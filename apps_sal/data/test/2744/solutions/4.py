from __future__ import division, print_function
import sys
import os
from io import BytesIO, IOBase
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange


class FastI(object):

    def __init__(self, fd=0, buffersize=2 ** 14):
        self.stream = stream = BytesIO()
        self.bufendl = 0

        def read2buffer():
            curpos = stream.tell()
            s = os.read(fd, buffersize + os.fstat(fd).st_size)
            stream.seek(0, 2)
            stream.write(s)
            stream.seek(curpos)
            return s
        self.read2buffer = read2buffer

    def read(self):
        while self.read2buffer():
            pass
        return self.stream.read() if self.stream.tell() else self.stream.getvalue()

    def readline(self):
        while self.bufendl == 0:
            s = self.read2buffer()
            self.bufendl += s.count(b'\n') + (not s)
        self.bufendl -= 1
        return self.stream.readline()

    def input(self):
        return self.readline().rstrip(b'\r\n')


class FastO(IOBase):

    def __init__(self, fd=1):
        stream = BytesIO()
        self.flush = lambda: os.write(1, stream.getvalue()) and (not stream.truncate(0)) and stream.seek(0)
        self.write = stream.write if py2 else lambda s: stream.write(s.encode())


(sys.stdin, sys.stdout) = (FastI(), FastO())
input = sys.stdin.readline


def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, len(heap) - 1)


def heappop(heap):
    lastelt = heap.pop()
    if not heap:
        return lastelt
    (returnitem, heap[0]) = (heap[0], lastelt)
    _siftup(heap)
    return returnitem


def heapreplace(heap, item):
    (returnitem, heap[0]) = (heap[0], item)
    _siftup(heap)
    return returnitem


def heappushpop(heap, item):
    if heap and heap[0] < item:
        (item, heap[0]) = (heap[0], item)
        _siftup(heap)
    return item


def heapify(x):
    for i in reversed(range(len(x) // 2)):
        _siftup(x, i)


def _siftdown(heap, pos):
    newitem = heap[pos]
    ppos = pos - 1 >> 1
    while pos and newitem < heap[ppos]:
        heap[pos] = heap[ppos]
        pos = ppos
        ppos = pos - 1 >> 1
    heap[pos] = newitem


def _siftup(heap, pos=0):
    newitem = heap[pos]
    leftchild = 2 * pos + 1
    rightchild = leftchild + 1
    while rightchild < len(heap):
        if heap[leftchild] < heap[rightchild]:
            heap[pos] = heap[leftchild]
            pos = leftchild
        else:
            heap[pos] = heap[rightchild]
            pos = rightchild
        leftchild = 2 * pos + 1
        rightchild = leftchild + 1
    if leftchild < len(heap):
        heap[pos] = heap[leftchild]
        pos = leftchild
    heap[pos] = newitem
    _siftdown(heap, pos)


s = sys.stdin.read().replace(b'\r', b'')
inp = []
numb = 0
for i in range(len(s)):
    if s[i] >= 48:
        numb = 10 * numb + s[i] - 48
    elif s[i] != 13:
        inp.append(numb)
        numb = 0
if s[-1] >= 48:
    inp.append(numb)
ind = 0
n = inp[ind]
ind += 1
m = inp[ind]
ind += 1
coupl = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for _ in range(m):
    v = inp[ind + 0] - 1
    u = inp[ind + 1] - 1
    w = 1.0 * inp[ind + 2]
    ind += 3
    coupl[v].append(u)
    coupl[u].append(v)
    cost[u].append(w)
    cost[v].append(w)
best = [1.0 * inp[ind + i] for i in range(n)]
Q = [(best[i], i) for i in range(n)]
heapify(Q)
while Q:
    (c, node) = heappop(Q)
    if best[node] != c:
        continue
    for j in range(len(coupl[node])):
        nei = coupl[node][j]
        C = c + 2 * cost[node][j]
        if C < best[nei]:
            best[nei] = C
            heappush(Q, (C, nei))
for x in best:
    sys.stdout.write(str(int(x)))
    sys.stdout.write(' ')

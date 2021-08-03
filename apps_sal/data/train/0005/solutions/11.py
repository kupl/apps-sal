import heapq
import sys


def ps(l):
    n = len(l)
    nxt = 1
    heap = []
    ans = []
    for i in range(n):
        heapq.heappush(heap, l[i])
        while heap and heap[0] == nxt:
            nxt += 1
            heapq.heappop(heap)
        if not heap:
            ans.append(i)
    return ans


for q in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    d = [int(i) for i in sys.stdin.readline().split()]
    st = set(ps(d))
    # print(st)
    d.reverse()
    anss = []
    ap = ps(d)
    # print(ap)
    for a in ap:
        b = n - 2 - a
        if b in st:
            anss.append(str(b + 1) + ' ' + str(n - b - 1) + '\n')
    sys.stdout.write(str(len(anss)) + '\n')
    sys.stdout.write(''.join(anss))

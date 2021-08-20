import collections
import heapq


class SegmentTree(object):

    def __init__(self, size):
        self.capacity = 1 << len(bin(size - 1)) - 2
        self.tree = [-1] * self.capacity * 2
        self.tree[0] = size
        self.left = set()
        p = self.capacity
        while p:
            self.left.add(p)
            p >>= 1

    def update(self, x, y):
        pos = self.capacity + x
        while pos:
            if y > self.tree[pos]:
                self.tree[pos] = y
            pos >>= 1

    def getmax(self, x):
        pos = self.capacity + x
        y = self.tree[pos]
        while pos:
            if y < self.tree[pos]:
                y = self.tree[pos]
            if pos & 1:
                pos = (pos >> 1) + 1
                if pos in self.left:
                    break
            else:
                pos >>= 1
        return y


def read_data():
    n = int(input())
    sxy = collections.defaultdict(list)
    for i in range(n):
        (x, y) = map(int, input().split())
        heapq.heappush(sxy[y - x], x)
    ws = list(map(int, input().split()))
    return (n, sxy, ws)


def solve(n, sxy, ws):
    path = []
    for w in ws:
        sxyw = sxy[w]
        if sxyw:
            x = heapq.heappop(sxy[w])
            y = w + x
            path.append((x, y))
        else:
            return False
    if is_valid(path):
        return path
    else:
        return False


def is_valid(path):
    xys = compress(path)
    segtree = SegmentTree(len(xys))
    for (x, y) in xys:
        maxy = segtree.getmax(x)
        if maxy >= y:
            return False
        segtree.update(x, y)
    return True


def compress(path):
    xset = set()
    for (x, y) in path:
        xset.add(x)
    xuniq = list(xset)
    xuniq.sort()
    dic = {x: i for (i, x) in enumerate(xuniq)}
    xys = [(dic[x], y) for (x, y) in path]
    return xys


(n, sxy, ws) = read_data()
result = solve(n, sxy, ws)
if result:
    print('YES')
    for (x, y) in result:
        print(x, y)
else:
    print('NO')

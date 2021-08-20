from heapq import heappop, heappush
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


class RangeAddQuery:

    def __init__(self, n):
        self.n0 = 2 ** (n - 1).bit_length()
        self.data = [0] * (2 * self.n0 - 1)

    def add(self, l, r, v):
        l += self.n0
        r += self.n0
        while l < r:
            if r & 1:
                r -= 1
                self.data[r - 1] += v
            if l & 1:
                self.data[l - 1] += v
                l += 1
            l >>= 1
            r >>= 1

    def query(self, i):
        i += self.n0 - 1
        res = 0
        while i + 1:
            if self.data[i]:
                res += self.data[i]
            i = ~-i // 2
        return res


(n, k) = list(map(int, input().split()))
m = 2 * 10 ** 5
RAQ = RangeAddQuery(m + 10)
segments = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    (a, b) = (a - 1, b - 1)
    RAQ.add(a, b + 1, 1)
    segments.append((a, b, i + 1))
segments.sort()
cursor = 0
heap = []
ans = []
for i in range(m):
    while cursor != n and segments[cursor][0] == i:
        heappush(heap, (-segments[cursor][1], segments[cursor][0], segments[cursor][2]))
        cursor += 1
    cnt = max(0, RAQ.query(i) - k)
    while cnt:
        (r, l, p) = heappop(heap)
        r = -r
        if r < i:
            continue
        RAQ.add(l, r + 1, -1)
        cnt -= 1
        ans.append(p)
print(len(ans))
print(*ans)

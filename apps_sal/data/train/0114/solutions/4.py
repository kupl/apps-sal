import sys
import bisect
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = 10**9

class RMQ:
    def __init__(self, a):
        self.n = len(a)
        self.size = 2**(self.n - 1).bit_length()
        self.data = [0] * (2*self.size-1)
        self.initialize(a)

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i]
        for i in range(self.size-2, -1, -1):
            self.data[i] = max(self.data[i*2 + 1], self.data[i*2 + 2])

    # Update ak as x
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = max(self.data[2*k+1], self.data[2*k+2])

    # max value in [l, r)
    def query(self, l, r):
        L = l + self.size; R = r + self.size
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                s = max(s, self.data[R-1])
            if L & 1:
                s = max(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(item) for item in input().split()]
    m = int(input())
    brave = []
    for j in range(m):
        pp, ss = [int(item) for item in input().split()]
        brave.append((pp, ss))
    brave.sort(reverse=True)
    p = []
    s = []
    for pp, ss in brave:
        p.append(pp)
        s.append(ss)
    s_rmq = RMQ(s)
    a_rmq = RMQ(a)
    p.reverse()
    s.reverse()
    max_step = max(s)
    days = 0
    curr = 0
    while curr < n:
        # Search step size
        l = 0; r = min(n - curr, max_step) + 1
        while r - l > 1:
            mid = (l + r) // 2
            max_monster = a_rmq.query(curr, curr+mid)
            index = m - bisect.bisect_left(p, max_monster)
            walkable = s_rmq.query(0, index)
            if walkable >= mid:
                l = mid
            else:
                r = mid
        if l == 0:
            days = -1
            break
        else:
            days += 1
            curr += l
    print(days)

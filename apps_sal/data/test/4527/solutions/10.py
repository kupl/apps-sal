from bisect import bisect_left as lower
import sys
input = sys.stdin.readline


def put():
    return list(map(int, input().split()))


def func(size, seg):
    dp = [[0] * size for i in range(size)]
    for k in range(1, size + 1):
        for l in range(size):
            r = l + k - 1
            if r < size:
                if l + 1 <= r:
                    dp[l][r] = dp[l + 1][r]
                same = 0
                for i in seg[l]:
                    if i == r:
                        same = 1
                    if i < r:
                        dp[l][r] = max(dp[l][r], dp[l][i] + dp[i + 1][r])
                dp[l][r] += same
    return dp[0][-1]


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        l, r, m = [], [], set()
        for i in range(n):
            x, y = put()
            l.append(x); r.append(y)
            m.add(x); m.add(y)
        m = sorted(m)
        size = len(m)
        seg = [[] for i in range(size)]
        for i in range(n):
            l[i] = lower(m, l[i])
            r[i] = lower(m, r[i])
            seg[l[i]].append(r[i])
        print(func(size, seg))


solve()

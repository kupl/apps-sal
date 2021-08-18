
from bisect import bisect_left, bisect_right
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
for i in range(Q):
    x = int(input())
    sl = float("-inf")
    sr = float("inf")
    tl = float("-inf")
    tr = float("inf")
    a = bisect_left(s, x)
    if a > 0:
        sl = s[a - 1]
    if a <= A - 1:
        sr = s[a]
    b = bisect_left(t, x)
    if b > 0:
        tl = t[b - 1]
    if b <= B - 1:
        tr = t[b]

    pat_LL = x - min(sl, tl)
    pat_LR = sr - tl + min(sr - x, x - tl)
    pat_RL = tr - sl + min(tr - x, x - sl)
    pat_RR = max(sr, tr) - x

    print(min(pat_LL, pat_LR, pat_RL, pat_RR))

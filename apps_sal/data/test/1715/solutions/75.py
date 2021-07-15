from bisect import bisect

A, B, Q = list(map(int, input().split()))
INF = 10 ** 18
S = [-INF]
T = [-INF]
for i in range(A):
    S.append(int(input()))
for i in range(B):
    T.append(int(input()))
S.append(INF)
T.append(INF)
for i in range(Q):
    x = int(input())
    sr = bisect(S, x)
    sl = sr - 1
    tr = bisect(T, x)
    tl = tr - 1
    def d(y): return abs(x - y)
    ans = min(d(max(S[sr], T[tr])), d(min(S[sl], T[tl])))
    ans = min(ans, 2 * d(S[sr]) + d(T[tl]))
    ans = min(ans, d(S[sr]) + 2 * d(T[tl]))
    ans = min(ans, 2 * d(S[sl]) + d(T[tr]))
    ans = min(ans, d(S[sl]) + 2 * d(T[tr]))
    print(ans)


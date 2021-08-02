from bisect import bisect, bisect_left

A, B, Q = map(int, input().split())
S, T, X = [0] * (A + 2), [0] * (B + 2), [0] * Q

INF = 10**10
S[0], T[0] = -INF, -INF
S[-1], T[-1] = 2 * INF, 2 * INF

for i in range(A):
    S[i + 1] = int(input())

for i in range(B):
    T[i + 1] = int(input())

for i in range(Q):
    X[i] = int(input())


def dis(x):
    RS = bisect_left(S, x)
    LS = RS - 1
    RT = bisect_left(T, x)
    LT = RT - 1
    ans = [0] * 4
    ans[0] = max(S[RS], T[RT]) - x
    ans[1] = x - min(S[LS], T[LT])
    ans[2] = S[RS] - T[LT] + min(S[RS] - x, x - T[LT])
    ans[3] = T[RT] - S[LS] + min(T[RT] - x, x - S[LS])
    return min(ans)


for x in X:
    print(dis(x))

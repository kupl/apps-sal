import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(input().rstrip()) for _ in range(Q)]

for S in Query:
    L = len(S)
    T = [(0, 0)]
    for s in S:
        x, y = T[-1]
        if s == "W":
            T.append((x, y + 1))
        elif s == "S":
            T.append((x, y - 1))
        elif s == "A":
            T.append((x - 1, y))
        else:
            T.append((x + 1, y))

    dp1 = [[0, 0, 0, 0] for _ in range(L + 1)]
    for i, (x, y) in enumerate(T):
        if i == 0:
            continue
        dp1[i][0] = max(y, dp1[i - 1][0])
        dp1[i][1] = min(y, dp1[i - 1][1])
        dp1[i][2] = min(x, dp1[i - 1][2])
        dp1[i][3] = max(x, dp1[i - 1][3])

    lx, ly = T[-1]
    dp2 = [[ly, ly, lx, lx] for _ in range(L + 1)]
    for i in reversed(range(L)):
        x, y = T[i]
        dp2[i][0] = max(y, dp2[i + 1][0])
        dp2[i][1] = min(y, dp2[i + 1][1])
        dp2[i][2] = min(x, dp2[i + 1][2])
        dp2[i][3] = max(x, dp2[i + 1][3])

    Y, X = dp1[L][0] - dp1[L][1] + 1, dp1[L][3] - dp1[L][2] + 1
    ans = 0
    for i in range(L):
        if dp1[i][0] < dp2[i][0] and dp1[i][1] < dp2[i][1]:
            ans = max(ans, X)
        if dp1[i][0] > dp2[i][0] and dp1[i][1] > dp2[i][1]:
            ans = max(ans, X)
        if dp1[i][2] < dp2[i][2] and dp1[i][3] < dp2[i][3]:
            ans = max(ans, Y)
        if dp1[i][2] > dp2[i][2] and dp1[i][3] > dp2[i][3]:
            ans = max(ans, Y)
    print(X * Y - ans)

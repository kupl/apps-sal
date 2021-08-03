N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
E = [[-1, ''] for _ in range(2 * N + 1)]
for i in range(1, N + 1):
    a, b = P[i - 1]
    if a != -1:
        if E[a][0] != -1:
            print("No")
            return
        else:
            E[a][0] = i
            E[a][1] = 'S'

    if b != -1:
        if E[b][0] != -1:
            print("No")
            return
        else:
            E[b][0] = i
            E[b][1] = 'G'

    if a >= b and a != -1 and b != -1:
        print("No")
        return

dp = [False] * (2 * N + 1)
dp[0] = True
for x in range(1, 2 * N + 1):
    for k in range(1, 2 * N + 1 - x):
        if x + 2 * k - 1 > 2 * N:
            continue
        ok = True
        for i in range(k):
            if E[x + i][0] != -1 and E[x + k + i][0] != -1 and E[x + i][0] != E[x + k + i][0]:
                ok = False
                break

            if E[x + i][1] == 'G':
                ok = False
                break

            if E[x + k + i][1] == 'S':
                ok = False
                break

        dp[x + 2 * k - 1] = dp[x + 2 * k - 1] or (dp[x - 1] and ok)

ans = 'Yes' if dp[2 * N] else 'No'
print(ans)

N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
need = [(0, 0)] * (N + 1)
now = 0
for i in range(N - 1):
    now += T[i]
    need[i + 1] = (now, min(V[i], V[i + 1]))
need[N] = (now + T[N - 1], 0)
TN = need[N][0]
res = [float('inf')] * (TN + 1)
for i in range(TN + 1):
    for j in range(N + 1):
        if j > 0:
            if need[j - 1][0] <= i <= need[j][0]:
                res[i] = min(res[i], V[j - 1])
        res[i] = min(res[i], need[j][1] + abs(need[j][0] - i))
ans = 0
for i in range(TN):
    if abs(res[i] - res[i + 1]) == 1:
        ans += 0.5 * (res[i] + res[i + 1])
    else:
        for j in range(N):
            if need[j][0] <= i and i + 1 <= need[j + 1][0]:
                vv = V[j]
                break
        if vv > res[i]:
            ans += res[i] + 0.25
        else:
            ans += res[i]
print(ans)

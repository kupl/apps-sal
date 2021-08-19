from math import ceil
(N, D, A) = list(map(int, input().split()))
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))
P.sort()
Attack = [-1 for _ in range(N)]
(leftx, leftj) = (0, 0)
for i in range(N):
    now = P[i][0]
    leftx = now + 2 * D
    while leftj < N:
        if P[leftj][0] <= leftx:
            leftj += 1
        else:
            break
    Attack[i] = leftj - 1
wk_dam = 0
imos = [0] * (N + 1)
ans = 0
for i in range(N):
    wk_dam += imos[i]
    if P[i][1] <= wk_dam:
        continue
    cnt = (P[i][1] - wk_dam + A - 1) // A
    wk_dam += cnt * A
    imos[i] += cnt * A
    imos[Attack[i] + 1] -= cnt * A
    ans += cnt
print(ans)

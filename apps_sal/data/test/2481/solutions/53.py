from collections import defaultdict
dicA = defaultdict(int)

H, W = map(int, input().split())
C = []
min_step = []
for i in range(10):
    temp = list(map(int, input().split()))
    C.append(temp)
    min_step.append(temp[1])


def dfs(n, k, now):
    if now > min_step[n]:
        return
    for i in range(10):
        if i == 1:
            min_step[n] = min(min_step[n], now + C[k][1])
        if i != k:
            if C[k][i] + now < min_step[n]:
                dfs(n, i, C[k][i] + now)


for i in range(10):
    if i == 1:
        continue
    for j in range(10):
        if i != j:
            dfs(i, j, C[i][j])


for i in range(H):
    temp = list(map(int, input().split()))
    for j in range(W):
        if temp[j] == -1:
            continue
        dicA[temp[j]] += 1
ans = 0
for x in dicA.keys():
    ans += min_step[x] * dicA[x]
print(ans)

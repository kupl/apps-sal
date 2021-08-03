from collections import defaultdict
dicA = defaultdict(int)

H, W = map(int, input().split())
C = []
min_step = []
for i in range(10):
    temp = list(map(int, input().split()))
    C.append(temp)
    min_step.append(temp[1])
# print(C)
# print(min_step)


def dfs(n, k, now):  # 0indexの数字nから1に行くのに最短の値。nowステップ進んで今kにいる。
    if now > min_step[n]:
        return
    for i in range(10):
        if i == 1:  # kから0に行ったときは、現状の最短とどちらが近いかを比較。
            #print(min_step[n],now+ C[k][1])
            min_step[n] = min(min_step[n], now + C[k][1])
        if i != k:
            if C[k][i] + now < min_step[n]:  # iを経由しても現状の最短よりも近い。
                # print(n,i,now,C[k][i])
                dfs(n, i, C[k][i] + now)


for i in range(10):
    if i == 1:
        continue
    for j in range(10):
        if i != j:
            dfs(i, j, C[i][j])

# print(min_step)

for i in range(H):
    temp = list(map(int, input().split()))
    for j in range(W):
        if temp[j] == -1:
            continue
        dicA[temp[j]] += 1  # 数字を0indexに
ans = 0
# print(dicA)
for x in dicA.keys():
    ans += min_step[x] * dicA[x]
print(ans)

n = int(input())
L = [[] for i in range(n + 1)]
for i in range(n - 1):
    (u, v, w) = map(int, input().split())
    L[u].append((v, w % 2))
    L[v].append((u, w % 2))
V = [0 for i in range(n + 1)]
V[1] = 1
ans = [0 for i in range(n + 1)]
que = [1]
head = 0
while len(que) > head:
    now = que[head]
    head += 1
    for nex in L[now]:
        if V[nex[0]] == 0:
            V[nex[0]] = 1
            ans[nex[0]] = ans[now] ^ nex[1]
            que.append(nex[0])
for pri in ans[1:]:
    print(pri)

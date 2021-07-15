N, k = map(int, input().split())
MOD = 10 ** 9 + 7
gr = [-1] * N
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b, c = map(int, input().split())
    if c == 0:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

g = 0
for i in range(N):
    if gr[i] == -1:
        que = [i]
        while que:
            j = que.pop()
            gr[j] = g
            for w in G[j]:
                if gr[w] == -1:
                    que.append(w)
        g += 1

num = 0
ans = (N ** k) % MOD
d = [0] * N
for i in range(N):
    if gr[i] != -1:
        d[gr[i]] += 1

for i in range(N):
    num += d[i] ** k
    num %= MOD

print((ans - num + MOD) % MOD)

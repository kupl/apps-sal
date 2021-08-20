def read():
    return map(int, input().split())


(n, m) = read()
G = [set() for i in range(n + 1)]
S = [0 for i in range(n + 1)]
for i in range(m):
    (a, b) = read()
    G[a].add(b)
    G[b].add(a)
    S[a] += 1
    S[b] += 1
ans = 10 ** 10
for i in range(1, n + 1):
    for j in G[i]:
        for k in G[j]:
            if i in G[k]:
                x = S[i] + S[j] + S[k] - 6
                ans = min(x, ans)
if ans == 10 ** 10:
    ans = -1
print(ans)

import collections
g = input().split()
N = int(g[0])
l = g[1]
S = [[0, 0, 0, 0] for i in range(N + 1)]
dic = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
X = [[0, 0] for i in range(N + 1)]
X[0] = tuple(X[0])
for i in range(1, N + 1):
    S[i] = S[i - 1].copy()
    S[i][dic[l[i - 1]]] += 1
    X[i][0] = S[i][0] - S[i][1]
    X[i][1] = S[i][2] - S[i][3]
    X[i] = tuple(X[i])
D = collections.Counter(X)
ans = 0
for v in D.values():
    ans += v * (v - 1) // 2
print(ans)

(n, m, q) = list(map(int, input().split()))
G = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    (l, r) = list(map(int, input().split()))
    G[l][r] += 1
S = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + G[i][j]
for i in range(q):
    (s, f) = list(map(int, input().split()))
    print(S[f][f] - S[s - 1][f] - S[f][s - 1] + S[s - 1][s - 1])

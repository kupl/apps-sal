n, m, Q = map(int, input().split())
lr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int, input().split())
    lr[l][r] += 1

rui = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        rui[i][j] = lr[i][j] + rui[i - 1][j] + rui[i][j - 1] - rui[i - 1][j - 1]
    
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    ans = rui[q][q] - rui[p][q] - rui[q][p] + rui[p][p]
    print(ans)

n, k = list(map(int, input().split()))
mod = 10 ** 9 + 7
max_n = 2050
comb = [[0] * max_n for i in range(max_n)]
for i in range(max_n):
    comb[i][1] = i
    comb[i][i] = 1
    comb[i][0] = 1
for i in range(1, max_n):
    for j in range(1, i):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % mod
for i in range(1, k+1):
    ans = comb[k-1][i-1]
    ans = (ans * comb[n-k+1][i]) % mod
    print(ans)


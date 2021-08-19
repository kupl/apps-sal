m = 10**5 + 5
cri = [0] * m
pri = []
for i in range(2, m):
    if cri[i] == 0:
        cri[i] = 1
        pri.append(i)
        for j in range(i, m, i):
            cri[j] = 1
dp = [0] * m
for a in range(len(pri) - 1):
    pa, pb = pri[a], pri[a + 1]
    for i in range(pa + 1, pb):
        dp[i] = pb - i
dp[0] = 2
dp[1] = 1
# print(dp[:10])
n, m = list(map(int, input().split()))
mat = [[dp[int(x)] for x in input().split()] for _ in range(n)]
res = min(sum(col) for col in mat)
for i in range(1, n):
    for j in range(m):
        mat[0][j] += mat[i][j]
print(min(min(mat[0]), res))

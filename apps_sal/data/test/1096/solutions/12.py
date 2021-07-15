import sys, math
f = [[1] * 10 for i in range(10)]
for i in range(10):
    f[0][i] = 0
    f[i][0] = 0
    f[9][i] = 0
    f[i][9] = 0
g = input()
a = ord(g[0]) - ord('a') + 1
b = int(g[1])
ans = f[a][b+1] + f[a+1][b] + f[a-1][b] + f[a][b-1] + f[a+1][b+1] + f[a-1][b+1] + f[a-1][b-1] + f[a+1][b-1]
print(ans)


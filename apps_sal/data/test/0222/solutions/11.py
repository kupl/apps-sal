import math


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


x = input()
ans = 0
for i in range(int(math.sqrt(int(x))), 0, -1):
    if lcs(x, str(i * i)) == len(str(i * i)):
        ans = len(str(i * i))
        break
if ans:
    print(len(x) - ans)
else:
    print(-1)

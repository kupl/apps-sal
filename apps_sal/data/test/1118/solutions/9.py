def lcs(a, b):
    c = [[0 for i in range(len(a) + 1)] for i in range(len(b) + 1)]
    for i in range(len(b) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c


n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    if a[i] != a[i - 1]:
        b.append(a[i])
a = b[::-1]
c = lcs(a, b)
ans = 0
n = len(a)
for i in range(0, n + 1):
    ans = max(ans, c[i][n - i])
print(n - ans - 1)

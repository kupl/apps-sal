n = int(input())
c = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    s = str(i)
    l = int(s[0])
    r = int(s[-1])
    c[l][r] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j] * c[j][i]

print(ans)

n = int(input())
a = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    s = str(i)
    a[int(s[0])][int(s[-1])] += 1
c = 0
for i in range(1, 10):
    for j in range(1, 10):
        c += a[i][j] * a[j][i]
print(c)

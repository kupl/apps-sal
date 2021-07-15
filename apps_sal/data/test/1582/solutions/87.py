n = int(input())
a = [[0 for i in range(10)] for j in range(10)]
for i in range(1, n+1):
    s = str(i)
    if s[-1] != '0':
        a[int(s[0])][int(s[-1])] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += a[i][j] * a[j][i]
print(ans)

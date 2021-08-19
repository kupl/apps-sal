m = int(input())
l = []
for i in range(m):
    l.append(list(input()))
ans = 0
for i in range(1, m - 1):
    for k in range(1, m - 1):
        if l[i][k] == 'X' and l[i - 1][k - 1] == 'X' and (l[i - 1][k + 1] == 'X') and (l[i + 1][k - 1] == 'X') and (l[i + 1][k + 1] == 'X'):
            ans += 1
print(ans)

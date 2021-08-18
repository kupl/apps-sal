n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, list(input()))))
m = int(input())
b = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if i != j and a[i][j] == 0:
            a[i][j] = 10**18
for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] = min(a[i][j], a[i][k] + a[k][j])
ans = []
for i in range(m):
    if i == 0 or i == m - 1:
        ans.append(b[i])
        continue
    x = ans[-1] - 1
    if(a[x][b[i] - 1] + a[b[i] - 1][b[i + 1] - 1] == a[x][b[i + 1] - 1]):
        continue
    ans.append(b[i])
print(len(ans))
print(*ans)

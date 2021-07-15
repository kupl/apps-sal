n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for l in range(n)]
ans = 0
for i in range(n):
    sum = c
    for j in range(m):
        sum += b[j]*a[i][j]
    if(sum > 0):
        ans = ans + 1
print(ans)

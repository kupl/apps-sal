n,m,c = list(map(int,input().split()))
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for i in range(n)]

ans = 0
for i in range(n):
    count = c
    for j in range(m):
        count += b[j]*a[i][j]
    if count > 0 :
        ans += 1

print(ans)


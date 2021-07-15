n,m,c = map(int,input().split())

b = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    a = [int(x) for x in input().split()]
    ans = c
    for j in range(m):
        ans += (a[j]*b[j])
    if(ans > 0):
        cnt += 1

print(cnt)

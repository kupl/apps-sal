n,m,c = map(int,input().split())
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    temp = 0
    a = list(map(int,input().split()))
    for j in range(m):
        temp += a[j]*b[j]
    if temp + c > 0:
        ans += 1
        
print(ans)

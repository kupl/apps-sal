n , k = list(map(int, input().split()))

if k==0:
    ans = (1+n-1)*(n-1)//2
else:
    ans = (1+n-k)*(n-k)//2


if k==0:
    for i in range(1,n+1):
        ans +=n//i

for i in range(k,n):
    if i==0:
        continue
    for j in range(1,n//i+1):
        if j*(i+1)+i<=n:
            ans+=(n-(j*(i+1)+i))//j+1
        if j*(i+1)+i>n:
            break

print(ans)


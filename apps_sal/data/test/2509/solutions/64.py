n,k = map(int,input().split())
if k ==0:
    print(n*n)
    return
ans = 0
for b in range(k+1,n+1):
    p = n//b
    r = n%b
    ans += max(b-k,0)*p + max(r+1-k,0)
print(ans)

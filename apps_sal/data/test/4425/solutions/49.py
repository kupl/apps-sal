n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    t = 1
    x = i
    while x<k:
        t*=0.5
        x*=2
    ans+=t/n
print(ans)

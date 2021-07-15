n=int(input())
a=list(map(int,input().split()))
ans=100000000
for i in range(-100,101):
    now=0
    for k in a:
        now+=(i-k)*(i-k)
    ans=min(ans,now)
print(ans)

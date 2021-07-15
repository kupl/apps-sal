n=int(input())
data=list(map(int,input().split()))
data.sort()
ans=0
for (i,x) in enumerate(data,2):
    ans+= x*i
ans-=data[-1]
print(ans)


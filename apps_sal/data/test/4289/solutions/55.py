n=str(input())
t,a=list(map(int,input().split()))
h=list(map(int,input().split()))
d=1000
ans=0
for index,x in enumerate(h):
    if abs(a-(t-x*0.006))<d:
        d=abs(a-(t-x*0.006))
        ans=index+1
print(ans)


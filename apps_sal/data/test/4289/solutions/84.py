n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))

ans=0
anst=10e7
for i,j in enumerate(h):
    avg=t-j*0.006
    if anst>abs(a-avg):
        anst=abs(a-avg)
        ans=i+1
print(ans)

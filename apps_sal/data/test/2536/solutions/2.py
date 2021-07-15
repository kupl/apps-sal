n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ans1=0
ans2=0
k=int(input())
c=0
d=0
for i in range(k):
    a,b=map(int,input().split())
    try:
        ans1+=l[a-1][b-1]
    except:
        c=1
    try:
        ans2+=l[b-1][a-1]
    except:
        d=1
if c:
    ans1=-1
if d:
    ans2=-1
print(max(ans1,ans2))
    


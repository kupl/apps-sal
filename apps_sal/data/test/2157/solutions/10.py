#in the name of god
#Mr_Rubick
n,q=list(map(int,input().split()))
t=[0]+list(map(int,input().split()))
p=[0]*(n+1)
for i in range(q):
    l,r=list(map(int,input().split()))
    p[l-1]+=1
    p[r]-=1
for i in range(1,n+1):
    p[i]+=p[i-1]
t.sort()
p.sort()
cnt=0
while p[cnt]==0:
    cnt+=1
print(sum(p[i]*t[i] for i in range(cnt,n+1)))


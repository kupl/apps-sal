n=int(input())
l=list(map(int,input().split()))
ll=[]
d={}
for i in range(n):
    for j in range(i+1,n):
        d[(l[i]+l[j])]=d.get((l[i]+l[j]),0)+1
mx=-1
for i in list(d.values()):
    if(i>mx):
        mx=i
print(mx)


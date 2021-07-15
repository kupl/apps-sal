q=int(input())
w=list(map(int,input().split()))
e=[0]*q
r=[]
t=[]
for i in range(q):
    if w[i]==0:r.append(i)
    else:e[w[i]-1]=1
for i in range(q):
    if e[i]==0:t.append(i)
for i in range(len(r)):
    if r[i]==t[i]:
        if i==0:t[i],t[1]=t[1],t[i]
        else:t[i],t[0]=t[0],t[i]
for i in range(len(r)):
    w[r[i]]=t[i]+1
print(*w)

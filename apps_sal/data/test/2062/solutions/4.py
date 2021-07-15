n=int(input())
l=list(map(int,input().split()))
l1=[0]*200001
for i in l:
    l1[i]+=1
for i in range(1,200001):
    l1[i]+=l1[i-1]
m=0
l=list(set(l))
for i in l:
    s=0
    for j in range(i,200001,i):
       s+=(l1[min(200000,i+j-1)]-l1[j-1])*j
    if(s>m):
        m=s
print(m)

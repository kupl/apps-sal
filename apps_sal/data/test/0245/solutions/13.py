
n=int(input())
c=[[],[],[],[]]
plos=0

for i in range(n):
    q=list(map(int,input().split()))
    plos+=(q[2]-q[0])*(q[3]-q[1])   
    for j in range(4):
        c[j].append(q[j]) 

fw=(max(c[2])-min(c[0]))
fh=(max(c[3])-min(c[1]))

if(fw==fh and fw*fh==plos):
    print("YES")
else:
    print("NO")

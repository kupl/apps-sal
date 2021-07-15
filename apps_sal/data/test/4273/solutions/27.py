N=int(input())
li=[0,0,0,0,0]
for i in range(N):
    S=input()
    if S[0]=="M":
        li[0]+=1
    if S[0]=="A":
        li[1]+=1
    if S[0]=="R":
        li[2]+=1
    if S[0]=="C":
        li[3]+=1
    if S[0]=="H":
        li[4]+=1
lim=0
for j in range(5):
    if li[j]!=0:
        lim+=1
temp=1   
li.sort(reverse=True)
ans=0
if lim==3:
    ans=li[0]*li[1]*li[2]
elif lim==4:
    lis=[[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
    for l in range(4):
        for m in range(3):
            temp*=li[lis[l][m]-1]
        ans+=temp
        temp=1
        
elif lim==5:
    lis=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
    for l in range(10):
        for m in range(3):
            temp*=li[lis[l][m]-1]
        ans+=temp
        temp=1
        
else:
    ans=0

print(ans)


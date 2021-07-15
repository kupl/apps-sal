import sys

n,k=list(map(int,input().split()))
s=input()

lcnt=-1
rcnt=-1

rr=[0]*n
ll=[0]*n
sim=""
for si in s:
    if si=="R" and sim=="R":
        rr[rcnt]+=1
    elif si=="R" and sim!="R":
        rcnt+=1
        rr[rcnt]=1
    if si=="L" and sim=="L":
        ll[lcnt]+=1
    elif si=="L" and sim!="L":
        lcnt+=1
        ll[lcnt]=1
    sim=si
        
ll=[i for i in ll if i!=0]
rr=[i for i in rr if i!=0]
#print(ll)
#print(rr)

minlen=min(len(ll),len(rr))
if minlen<=k:
    print((n-1))
    return
    
for i in range(k):
    ll[i]+=rr[i]
    rr[i]=0

for i in range(len(ll)-1):
    if i<len(rr) and ll[i]!=0 and rr[i]==0 :
        ll[i+1]+=ll[i]
        ll[i]=0

icnt=0
for i in range(len(ll)):
    icnt+=max(ll[i]-1,0)
for i in range(len(rr)):
    icnt+=max(rr[i]-1,0)
    
print(icnt)


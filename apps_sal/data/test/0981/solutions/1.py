import sys
v=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))

ind=1
vol=A[0]

for i in range(1,10):
    if(A[i-1]<vol):
        vol=A[i-1]
        ind=i
    elif(A[i-1]==vol and i>ind):
        vol=A[i-1]
        ind=i

used=(v//vol)*vol

rest=v-used

x=rest-1
z=0
ans=list(str(ind)*(v//vol))

while(len(ans)!=0 and x!=rest and z<len(ans)):
    x=rest
    for i in range(9,0,-1):
        if(A[i-1]-A[ind-1]<=rest):
            rest-=A[i-1]-A[ind-1]
            ans[z]=str(i)
            z+=1
            break
Ans=""
for item in ans:
    Ans+=item
if(len(Ans)==0):
    print(-1)
else:
    sys.stdout.write(Ans)



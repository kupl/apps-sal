from heapq import*
L,R=[],[]
n=int(input())
B=0
cnt=0
l,r=0,0
for i in range(n):
    I=input()
    if I[0]=="1":
        a,b,c=map(int,I.split())
        B+=c
        cnt+=1
        
        if cnt%2:
            x=heappushpop(R,b)
            r+=b-x
            heappush(L,-x)
            l+=-x
        else:
            x=heappushpop(L,-b)
            l+=-b-x
            heappush(R,-x)
            r+=-x
        #print(L,R,l,r)
        #print(b,x)
    else:
        med=-L[0]
#        print(L,R)
#        print(l,r)
        print(med,cnt%2*med+B+l+r)

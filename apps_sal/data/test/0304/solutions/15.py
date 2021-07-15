ct=[0]*10
fact=[1]*20
ans=0
def setAns(lol):
    nonlocal ans
    ans=lol

def calc(k,fr):
    if(k==10):
        # print(fr)
        tot=sum(fr)
        w0=fact[tot]
        # print(tot,w0)
        for i in range(10):
            w0//=fact[fr[i]]
        wo0=0
        if(fr[0]>0):
            fr[0]-=1
            wo0=fact[tot-1]
            for i in range(10):
                wo0//=fact[fr[i]]
            fr[0]+=1
        tp=w0-wo0
        # print(w0,wo0)
        setAns(ans+tp)
        return
    if(ct[k]==0):
        calc(k+1,fr)
        return 
    for i in range(1,ct[k]+1):
        # print(k,i)
        fr[k]=i
        calc(k+1,fr)

fact[0]=1
for i in range(1,20):
    fact[i]=fact[i-1]*i
n=int(input())
while(n>0):
    k=n%10
    n//=10
    ct[k]+=1
freq=[0]*10
calc(0,freq)
print(ans)

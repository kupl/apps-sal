q=int(input())
l=[]
r=[]

def primecheck(n):
    if n==1:
        return False
    else:
        i=2
        ok=True
        while i*i<=n:
            if n%i==0:
                ok=False
                return ok
            i+=1
        if ok:
            return True
mx=0
for i in range(q):
    L,R=list(map(int,input().split()))
    l.append(L)
    r.append(R)
    mx=max(mx,R)

memo=[0]*(mx+1)
for i in range(1,mx+1):
    if primecheck(i) and primecheck((i+1)//2):
        memo[i]=memo[i-1]+1
    else:
        memo[i]=memo[i-1]
    
for i in range(q):
    print((memo[r[i]]-memo[l[i]-1]))


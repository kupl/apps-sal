import itertools as it
S=input().strip()
freq=[0 for i in range(10)]
for i in S:
    u=ord(i)-ord('0')
    freq[u]+=1

fac=[1]
for i in range(1,20): fac.append(i*fac[-1])

"""
M={}
def F(cur,used):
    while cur<10 and freq[cur]==0: cur+=1
    if cur==10:
        r=fac[sum(used)]
        for i in used:
            r//=fac[i]
        print(used)
        return 1

    key=(cur,tuple(used))
    if key in M: return M[key]
    
    r=0
    for i in range(1,freq[cur]):
        for j in range(
    return r

total=0
for i in range(1,10):
    if freq[i]==0: continue
    M={}
    freq[i]-=1
    used=[0 for j in range(10)]
    used[i]=1
    total+=F(0,used)
    freq[i]+=1

print(total)
"""

total=0
for x in it.product(*(list(range(0 if i==0 else 1,i+1)) for i in freq)):
    Q="".join(str(i)*x[i] for i in range(10))
    s=sum(x)-1
    if s<0: continue
    g=0
    for d in range(1,10):
        n=fac[s]
        y=list(x)
        y[d]-=1
        #assert(s==sum(y))
        for k in range(0,10):
            n//=fac[y[k]]
        g+=n
        #print(x,d,n,g)
    #print(Q,x,g)
    total+=g

print(total)

#208
#280
#802
#820
#2028, 2082, 2208, 2280, 2802, 2820
#8022, 8202, 8220


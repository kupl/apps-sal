N=int(input())
mod=10**9+7

ANSLIST=[1]
for i in range(61):
    ANSLIST.append((ANSLIST[-1]*3-1)%mod)

ANS=[1, 2, 4, 5]
ANSDICT=dict()
def ans(k):
    if 0<=k<=3:
        return ANS[k]
    if ANSDICT.get(k)!=None:
        return ANSDICT[k]
    for i in range(61):
        if k==2**i-2:
            return ANSLIST[i]-1
        if k==2**i-1:
            return ANSLIST[i]
        if 2**i-1>k:
            break
    x=k-(2**(i-1)-1)

    ANSDICT[k]=(ans(x-1)+ANSLIST[i-1]*2-ans(2**(i-1)-x-2)-1)%mod
    return ANSDICT[k]

print(ans(N))

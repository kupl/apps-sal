n,k=list(map(int,input().split()))
lis=list(map(int,input().split()))

ins=[0 for i in range(10**6)]
ins[lis[0]]+=1
zeroes=10**6-1
mL=0
pair=[0,0]
r=0
for l in range(n):

    if l>0:
        ins[lis[l-1]]-=1
        if ins[lis[l-1]]==0:
            zeroes+=1

    while 10**6-zeroes<=k and r<n-1:
        r+=1
        ins[lis[r]]+=1
        if ins[lis[r]]==1:
            zeroes-=1

        if 10**6-zeroes==k+1:
            ins[lis[r]]-=1
            zeroes+=1
            r-=1
            break

    if mL<r-l:
        mL=r-l
        pair=[l,r]

print(pair[0]+1,pair[1]+1)


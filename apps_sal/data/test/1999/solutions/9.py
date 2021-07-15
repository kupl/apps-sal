n=int(input().split()[0])
ns=[int(x) for x in input().split()[:n]]
ind={}
i=0
while i<n:
    ni=ns[i]
    while ni in ind:
        ns[ind[ni]]=None
        ind.pop(ni, None)
        ni*=2
    ns[i]=ni
    ind[ni]=i
    i+=1
ans=[x for x in ns if x!=None]
print(len(ans))
for i in ans:
    print(i,end=' ')



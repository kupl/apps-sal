init=int(input())

ans=[]
for K in range(2,int(init**0.5)+1):
    N=init
    while N%K==0:
        N/=K
    if N-(N//K)*K==1:
        ans.append(K)
        
tgt=init-1
cand=[]
for i in range(1,int(init**0.5)+1):
    if tgt%i==0:
        cand.append(i)
        if i!=tgt//i:
            cand.append(tgt//i)
ans=list(set(ans+cand))
print((len(ans)))



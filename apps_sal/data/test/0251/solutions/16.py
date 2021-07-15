n,k=[int(x) for x in input().split()]

d={}
ns=[int(x) for x in input().split()]
minn=min(ns)
ns=[x-minn for x in ns]

for c in ns:
    if c in d:
        d[c]+=1
    else:
        d[c]=1

def eat(i,need):
    al=(ns[i]-ns[i+1])*d[ns[i]]
    if al>need:
        thick=d[ns[i]]
        eath=need//thick
        d[ns[i] - eath]=d[ns[i]]
        ns[i]-=eath
        return i,0
    if al==need:
        d[ns[i+1]]+=d[ns[i]]
        return i+1,0
    if al<need:
        d[ns[i + 1]] += d[ns[i]]
        return i+1,need-al


ns=list(d.keys())
ns.sort(reverse=True)




ans=0

i=0
newn=k

while i<len(ns)-1:
    i,newn=eat(i,newn)
    if newn>0 and i>=len(ns)-1:
        ans+=1
        break
    if newn==0:
        ans+=1
        newn=k





print(ans)






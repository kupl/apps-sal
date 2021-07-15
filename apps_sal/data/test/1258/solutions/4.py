n=int(input())
d={}
used=set()
for itr in range(n-2):
    p,q,r=map(int,input().split())
    if p in d: d[p].append([p,q,r])
    else: d[p]=[[p,q,r]]
    if q in d: d[q].append([p,q,r])
    else: d[q]=[[p,q,r]]
    if r in d: d[r].append([p,q,r])
    else: d[r]=[[p,q,r]]
ans=[]
for itr in d:
    if len(d[itr])==1: 
        k=itr
        break
ans.append(k)
used.add(frozenset(d[k][0]))
for itr in d[k][0]:
    if itr==k: continue
    ans.insert(len(d[itr])-1,itr)
for itr in range(1,n-2):
    for tup in d[ans[itr]]:
        if frozenset(tup) in used: continue
        for i in tup:
            if i==ans[itr] or i==ans[itr+1]: continue
            ans.append(i)
        used.add(frozenset(tup))
print(*ans)

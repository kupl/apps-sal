def I():
    return int(input())
def IS():
    return  input()
def IL():
    return list(map(int,input().split()))
def IM():
    return list(map(int,input().split()))
n,k=IM() 
l=IL() 
from collections import Counter
c=Counter(l)
if max(c.values())>=k:
    print(0)
    return 
l.sort() 
from collections import defaultdict 
d=defaultdict(list)
for i in range(n):
    curr=l[i]
    while curr:
        d[(l[i],i)].append(curr)
        curr//=2 
    d[(l[i],i)].append(0)
mini=10**9 
def check(i):
    to_make=i 
    tot=[] 
    for j in range(n):
        if i not in d[(l[j],j)]:
            pass 
        else:
            tot.append(d[(l[j],j)].index(i))
    if len(tot)<k:
        return 10**9
    else:
        tot.sort()
        return sum(tot[:k])
d1=defaultdict(int)
for i in d:
    a=d[i]
    for a1 in a:
        d1[a1]+=1 
cand=[i for i in d1 if d1[i]>=k]
#print(cand)
for i in l:
    mini=min(mini,check(i))
for i in range(1000):
    mini=min(mini,check(i))
for i in cand:
    mini=min(mini,check(i))
print(mini)


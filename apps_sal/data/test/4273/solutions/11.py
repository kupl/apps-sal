import collections
import itertools
n=int(input())
l,s=[],[]
for i in range(n):
    a=input()
    if a[0]=="M" or a[0]=="A" or a[0]=="R" or a[0]=="C" or a[0]=="H":
        l.append(a[0])
        if s.count(a[0])==0:
            s.append(a[0])
l=collections.Counter(l)
ans=0
for j in itertools.combinations(s,3):
    ans+=(l[j[0]]*l[j[1]]*l[j[2]])
print(ans)


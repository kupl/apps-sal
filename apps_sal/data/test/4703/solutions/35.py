S=input()
l=len(S)

ls=[i for i in range(1,l)]
    
sa=[]
for i in range(len(S)):sa+=[S[i],'']
sa=sa[:-1]

import copy
import itertools as it
ans=0
for i in range(l):
 for j in it.combinations(ls, i):
    sx=copy.copy(sa)
    for k in j:sx[2*k-1]='+'
    ans+=eval(''.join(sx))
print(ans)

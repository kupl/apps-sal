import operator
from collections import Counter
n,k=[int(_) for _ in input().split()]
D=Counter([int(_) for _ in input().split()])
D=dict(sorted(list(D.items()), key=operator.itemgetter(1),reverse=True))
c=0
i=0
for _ in D:
    if i>=k:
        c+=D[_]
    i+=1
print(c)


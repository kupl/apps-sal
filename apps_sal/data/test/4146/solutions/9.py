N=int(input())
Z=list(map(int,input().split()))
from collections import Counter
c=Counter(Z[::2]).most_common(2)+[(0,0)]
c2=Counter(Z[1::2]).most_common(2)+[(0,0)]
if c[0][0]!=c2[0][0]:
    print(N-c[0][1]-c2[0][1])
else:
    print(min(N-c[1][1]-c2[0][1],N-c[0][1]-c2[1][1]))

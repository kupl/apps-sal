"""
NTC here
"""
from sys import setcheckinterval, stdin
setcheckinterval(1000)

# print("Case #{}: {} {}".format(i, n + m, n * m))

iin = lambda: int(stdin.readline())
lin = lambda: list(map(int, stdin.readline().split()))


s,b=lin()
sa=lin()
ba=[lin() for i in range(b)]
ba.sort()
ans=[]
sol=[]
for i,j in ba:
    sol.append(i)
    ans.append(j)
for i in range(1,b):
    ans[i]+=ans[i-1]

from bisect import bisect_right
a=[]
for i in sa:
    x=bisect_right(sol,i)-1
    #print(x,ans)
    if x<0:
        a.append(0)
    else:
        a.append(ans[x])
print(*a)

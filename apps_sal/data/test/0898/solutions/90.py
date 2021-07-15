from math import sqrt
from math import floor
n,m = map(int,input().split())
d = m // n
ans = 1
for i in range(1,floor(sqrt(m))+1):
    if m % i == 0:
        x = m // i
        if i <= d:
            ans = max(ans,i)
        if x <= d:
            ans = max(ans,x)
print(ans)

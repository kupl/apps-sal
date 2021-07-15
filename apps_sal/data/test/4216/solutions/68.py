N = int(input())
f = lambda x,y:len(str(x)) if x > y else len(str(y))
from math import floor, sqrt
ans = len(str(N))
for a in range(1,floor(sqrt(N))+1):
    if N % a == 0:
        ans = min(ans, f(a,N//a))
print(ans)

import sys
from itertools import accumulate
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
a = [i-1 for i in a]
suma = [0]+list(accumulate(a))
suma = [i%k for i in suma]
rem = defaultdict(int)
ans = 0
if k > n:
    for i in range(n+1):
        x = suma[i]
        rem[x] += 1
    for s in rem.values():
        ans += s*(s-1)//2
    print(ans)
    return
for i in range(k):
    x = suma[i]
    rem[x] += 1
for s in rem.values():
    ans += s*(s-1)//2
for i in range(n-k+1):
    rem[suma[i]%k] -= 1
    rem[suma[i+k]%k] += 1
    ans += rem[suma[i+k]] -1
print(ans)

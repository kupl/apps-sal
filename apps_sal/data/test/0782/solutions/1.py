from fractions import gcd
from functools import reduce

m = int(input())
a = list(map(int, input().split()))
ans = []

if reduce(gcd, a) == a[0]:
    for i in range(1, m):
        ans.append(a[0])
        ans.append(a[i])
    ans.append(a[0])
    print(len(ans))
    print(' '.join(map(str, ans)))
else:
    print(-1)

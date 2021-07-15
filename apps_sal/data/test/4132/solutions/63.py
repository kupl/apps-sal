n=int(input())
a=list(map(int,input().split()))

import math
ans = a[0]
for i in range(1, n):
    ans = math.gcd(ans, a[i])
print(ans)

n = int(input())
from math import gcd
As = list(map(int, input().split()))
ans = As[0]
for a in As:
    ans = gcd(ans,a)
print(ans)

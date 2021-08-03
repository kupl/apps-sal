from math import gcd
n = int(input())
a = [int(i) for i in input().split()]
ans = a[0]
for i in a:
    ans = gcd(ans, i)
print(ans)

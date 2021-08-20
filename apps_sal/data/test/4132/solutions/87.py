from math import gcd
n = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans = gcd(ans, a)
print(ans)

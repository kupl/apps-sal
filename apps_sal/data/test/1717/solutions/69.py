from math import gcd
n = int(input())
ans = 1
for i in range(1, n + 1):
    ans = (ans * i) // gcd(ans, i)
print(ans + 1)

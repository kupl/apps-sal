

from math import gcd as g


k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        temp = g(a, b)
        for c in range(1, k+1):
            ans += g(temp, c)


print(ans)


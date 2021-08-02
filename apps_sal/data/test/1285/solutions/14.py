from math import gcd
import sys
n = int(sys.stdin.readline())
a = [[] for i in range(n)]
for i in range(n):
    a[i] = bin((1 << n) | int(sys.stdin.readline(), 16))[3:]


ans, i = 0, 0
while i < n:
    j = i + 1
    while j < n and a[i] == a[j]:
        j += 1
    ans = gcd(ans, j - i)

    k = 0
    while k < n:
        l = k + 1
        while l < n and a[i][k] == a[i][l]:
            l += 1
        ans = gcd(ans, abs(l - k))
        k = l
    i = j
print(ans)

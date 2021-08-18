import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


n = int(input())
d = int(input())
e = int(input())

dollar = d
euro = 5 * e

ans = n

if n % dollar == 0 or n % euro == 0:
    print(0)
    return

for i in range(n // dollar + 1):
    k = n - i * dollar
    k -= (k // euro) * euro

    ans = min(ans, k)

for i in range(n // euro + 1):
    k = n - i * euro
    k -= (k // dollar) * dollar

    ans = min(ans, k)


print(ans)

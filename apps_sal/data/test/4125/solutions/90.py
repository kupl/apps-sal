import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a.sort()
d = set()
for i in range(n):
  d.add(a[i + 1] - a[i])
d = list(d)
ans = gcd_list(d)
print(ans)

import math
from functools import reduce

n, m = map(int, input().split())


t = [int(x) for x in input().split()]

p = [int(x) for x in input().split()]

tt = reduce(math.gcd, [x - t[0] for x in t])

for i, pp in enumerate(p, start=1):
    if tt % pp == 0:
        print("YES")
        print(t[0], i)
        break

else:
    print("NO")

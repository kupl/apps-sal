import math
from functools import reduce

n, x = map(int, input().split())
X = sorted(list(map(int, input().split())) + [x])

print(reduce(math.gcd,[X[i+1]-X[i] for i in range(n)]))

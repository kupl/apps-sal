import math
import functools
N = int(input())
A = list(map(int, input().split()))
ans = functools.reduce(math.gcd, A)
print(ans)

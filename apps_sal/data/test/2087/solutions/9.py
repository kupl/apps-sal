import math
from collections import Counter
import itertools

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

a, b, c = mi()
ans = (a * (a + 1) // 2) * (b * (b + 1) // 2) * (c * (c + 1) // 2)
print(ans % 998244353)

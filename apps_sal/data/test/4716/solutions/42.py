import sys
from typing import List

n, k = list(map(int, input().split()))
ll = list(map(int, input().split()))

bar = sorted(ll)[::-1]
#bar2 = bar[::-1]
ans = sum(bar[0:k])

print(ans)

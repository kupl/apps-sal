
from bisect import bisect_left
import sys
N = int(input())
c = input().strip()
ans = 0
r = [i for i, x in enumerate(c) if x == 'R']
r_num = len(r)

ans = bisect_left(r, r_num)
print(r_num - ans)

from itertools import groupby
from math import ceil
(n, k) = list(map(int, input().split()))
s = input()
block = [sum((1 for _ in it)) for (k, it) in groupby(s)]
if s[0] != '1':
    block.insert(0, 0)
m = len(block)
(left, right) = (0, 2 * k)
res = val = sum(block[left:right - 1])
while right <= m:
    val += block[right - 1] if right == m else block[right - 1] + block[right]
    res = max(res, val)
    val -= block[left] + block[left + 1]
    left += 2
    right += 2
print(res)

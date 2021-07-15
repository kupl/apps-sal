from itertools import accumulate
from operator import xor
n = int(input())
l = accumulate([1 if x < 0 else 0 for x in map(int, input().split())], xor)
a = b = 0
cnt = [1, 0]
for e in l:
    a += cnt[e ^ 1]
    b += cnt[e]
    cnt[e] += 1
print(a, b)


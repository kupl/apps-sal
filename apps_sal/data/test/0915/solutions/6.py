from math import *
from random import *
s = "codeforces"
n = len(s)
k = int(input())
cnt = [1 for i in range(n)]
mlt = 1
pos = 0
while mlt < k:
    mlt //= cnt[pos]
    cnt[pos] += 1
    mlt *= cnt[pos]
    pos += 1
    if pos >= n:
        pos -= n
for i in range(n):
    for j in range(cnt[i]):
        print(s[i], end='')

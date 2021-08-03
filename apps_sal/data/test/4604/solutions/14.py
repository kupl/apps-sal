import sys
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
a.sort()

l = []

for i in range(n):
    li = abs(i - (n - 1 - i))
    l.append(li)

l.sort()


for ai, li in zip(l, a):
    if ai != li:
        print((0))
        return

d = Counter(l)
mod = 10 ** 9 + 7
ans = 1

for li in d:
    for j in range(1, d[li] + 1):
        ans *= j
        ans %= mod

print(ans)

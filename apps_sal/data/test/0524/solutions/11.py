from collections import Counter
import math
n = int(input())
l = list(map(int, input().split()))
l.sort()
m = l[-1]
p = m ** (1 / (n - 1))
ans = math.ceil(p)
ans1 = int(p)
c1 = 0
c2 = 0
for i in range(n):
    if ans ** i != l[i]:
        c1 += abs(ans ** i - l[i])
for i in range(n):
    if ans1 ** i != l[i]:
        c2 += abs(ans1 ** i - l[i])
print(min(c1, c2))

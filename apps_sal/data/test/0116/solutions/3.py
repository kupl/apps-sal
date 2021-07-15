import sys, math
l1, r1, l2, r2, k = map(int,input().split())
a = max(l1, l2)
b = min(r1, r2)
ans = b - a + 1
if a <= k <= b:
    ans -= 1
print(max(0, ans))

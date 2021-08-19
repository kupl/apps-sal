import math
n = int(input())
a = list(map(int, input().split()))
sunuke = 0
kuma = sum(a)
memo = abs(2 * a[0] - sum(a))
ans = abs(2 * a[0] - sum(a))
for i in range(n):
    sunuke += a[i]
    kuma -= a[i]
    if abs(sunuke - kuma) > memo:
        ans = memo
    else:
        memo = abs(sunuke - kuma)
print(ans)

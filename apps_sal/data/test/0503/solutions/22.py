from collections import Counter

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]


lk = {}
ans = 0

rk = Counter(a)

for x in a:
    rk[x] -= 1
    if x % k == 0:
        ans += lk.get(x / k, 0) * rk.get(x * k, 0)
    lk[x] = 1 + lk.get(x, 0)

print(ans)

k2, k3, k5, k6 = [int(x) for x in input().split()]
c1 = min(k2, k5, k6)
ans = c1 * 256
k2 -= c1
if k2 > 0:
    ans += 32 * (min(k2, k3))
print(ans)

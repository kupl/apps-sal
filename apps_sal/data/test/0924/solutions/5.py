import math

la, ra, ta = list(map(int, input().split()))
lb, rb, tb = list(map(int, input().split()))
if rb - lb < ra - la:
    la, ra, ta, lb, rb, tb = lb, rb, tb, la, ra, ta
t = math.gcd(ta, tb)

def sect(k):
    return max(0, min(rb, ra + k * t) - max(lb, la + k * t) + 1)

ans = max(sect(x) for x in [(rb - ra) // t, (lb - la + t - 1) // t])
print(ans)


3

from fractions import gcd

cnt1, cnt2, a, b = tuple(map(int, input().split()))
lcm = a*b // gcd(a, b)

def check(v):
    c1 = int(v/b) - int(v/lcm)
    c2 = int(v/a) - int(v/lcm)
    rest = v - c1 - c2 - int(v/lcm)
    c1 = min(c1, cnt1)
    c2 = min(c2, cnt2)
    return rest >= cnt1+cnt2-c1-c2

left, right = 1, 10**18
while left + 1 < right:
    mid = (left+right) // 2
    if (check(mid)):
        right = mid
    else:
        left = mid
print(right)


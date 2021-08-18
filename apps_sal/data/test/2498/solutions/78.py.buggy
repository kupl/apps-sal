from math import gcd
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
lcm = 1
for a in A:
    lcm = lcm * a // gcd(lcm, a)
    if lcm > M * 2:
        print((0))
        return
for a in A:
    if lcm // a % 2 == 0:
        print((0))
        return
ans = M // (lcm // 2) - M // lcm
print(ans)

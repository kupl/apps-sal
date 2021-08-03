n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


def gcd(num1, num2):
    r = 1
    while r > 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


def lcm(num1, num2):
    gcd1 = gcd(num1, num2)
    return num1 * num2 // gcd1


lcm1 = a[0] // 2
lcm2 = a[0]

for i in range(1, n):
    t = a[i]
    lcm1 = lcm(lcm1, t // 2)
    lcm2 = lcm(lcm2, t)
    ta = max(t // 2, lcm1)
    tb = min(t // 2, lcm1)
    if ta != tb and ta // tb % 2 == 0:
        lcm1 = 0
        lcm2 = 0
        break

if lcm1 != 0:
    ans1 = m // lcm1
    ans2 = m // lcm2
    ans = ans1 - ans2
else:
    ans = 0

print(ans)

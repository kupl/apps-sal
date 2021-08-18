import math

n = int(input())

mod = 10**9 + 7

data = {}
zero_zero = 0

for i in range(n):
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        zero_zero += 1
        continue
    gcd = math.gcd(a, b)
    a, b = a // gcd, b // gcd
    if a < 0:
        a, b = -a, -b

    if a == 0:
        a, b = 0, 1

    elif b == 0:
        a, b = 1, 0

    if b <= 0:
        if (-b, a) in data:
            data[(-b, a)][1] += 1
        else:
            data[(-b, a)] = [0, 1]
    elif b > 0:
        if (a, b) in data:
            data[(a, b)][0] += 1
        else:
            data[(a, b)] = [1, 0]


power_2 = [1]
for i in range(1, 2 * 10**5 + 100):
    power_2.append(power_2[i - 1] * 2 % mod)

ans = 1
for (a, b), (l, m) in list(data.items()):
    ans *= (power_2[l] + power_2[m] - 1) % mod

ans = ans - 1
ans += zero_zero
print((ans % mod))

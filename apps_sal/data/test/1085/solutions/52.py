from math import ceil


def enum_divisor(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i != 0:
            continue
        res.append(i)
        if i * i != n:
            res.append(n // i)
    return res


ans = 0
n = int(input())
for x in enum_divisor(n):
    if x == 1:
        continue
    tmp = n
    while tmp % x == 0:
        tmp //= x
    if tmp % x == 1:
        ans += 1
ans += len(enum_divisor(n - 1)) - 1
print(ans)

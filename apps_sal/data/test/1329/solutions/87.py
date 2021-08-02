import collections

n = int(input())


def division(n):
    if n < 2:
        return []

    prime_factors = []

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)

    return prime_factors


num = []

for i in range(1, n + 1):
    div = division(i)
    num.extend(div)
c = collections.Counter(num)

div_num = 1

n2, n4, n14, n24, n74 = 0, 0, 0, 0, 0

for k, v in c.items():
    if 2 <= v:
        n2 += 1
    if 4 <= v:
        n4 += 1
    if 14 <= v:
        n14 += 1
    if 24 <= v:
        n24 += 1
    if 74 <= v:
        n74 += 1

ans = n74 + n24 * (n2 - 1) + n14 * (n4 - 1) + n4 * (n4 - 1) * (n2 - 2) // 2

print(ans)

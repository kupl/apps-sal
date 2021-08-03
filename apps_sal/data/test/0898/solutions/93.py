n, m = map(int, input().split())

x = m // n


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


y = make_divisors(m)

res = 1

for i in y:
    if i <= x:
        res = i

print(res)

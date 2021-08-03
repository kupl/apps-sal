n = int(input())


def f(a, b):
    a = list(str(a))
    b = list(str(b))
    return max(len(a), len(b))


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


l = make_divisors(n)
if len(l) % 2 == 0:
    m = float('inf')
    for i in range(len(l) // 2):
        m = min(m, f(l[i], n // l[i]))
    print(m)
else:
    m = float('inf')
    for i in range(len(l) // 2 + 1):
        m = min(m, f(l[i], n // l[i]))
    print(m)

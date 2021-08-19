# import sympy

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


n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        # if len(sympy.divisors(i)) == 8:
        if len(make_divisors(i)) == 8:
            count += 1
print(count)

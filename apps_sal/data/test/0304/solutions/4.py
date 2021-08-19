import itertools as it


def factorial(n):
    i = 1
    for j in range(1, n + 1):
        i *= j
    return i


def C(n, k):
    k = max([k, n - k])
    result = 1
    for i in range(k + 1, n + 1):
        result *= i
    result //= factorial(n - k)
    return result


n = input()
digits = [0 for _ in range(10)]
for i in n:
    digits[int(i)] += 1
result = 0
for amounts in it.product(*[[0] if x == 0 else list(range(1, x + 1)) for x in digits]):
    sum_no_zero = sum(amounts[1:])
    if sum_no_zero == 0:
        continue
    tmp = factorial(sum_no_zero)
    for j in amounts[1:]:
        tmp //= factorial(j)
    tmp *= C(sum_no_zero + amounts[0] - 1, amounts[0])
    result += tmp
print(result)

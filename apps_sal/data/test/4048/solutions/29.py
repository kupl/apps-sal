import sys


def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


input = sys.stdin.readline
n = int(input())
yaku_list = make_divisors(n)
index = int(len(yaku_list) / 2)
if len(yaku_list) % 2 == 0:
    result = yaku_list[index - 1] - 1 + yaku_list[index] - 1
else:
    result = yaku_list[index] - 1 + yaku_list[index] - 1
print(result)

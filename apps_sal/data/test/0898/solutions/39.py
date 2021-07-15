N, M = list(map(int, input().split()))


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

div_list = make_divisors(M)
div_list = div_list[::-1]
for div in div_list:
    if N * div <= M:
        print(div)
        return


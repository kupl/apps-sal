n, m = list(map(int, input().split()))


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


l = make_divisors(m)

l.reverse()


for x in l:
    if m // x >= n:
        print(x)
        break

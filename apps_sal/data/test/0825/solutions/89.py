import collections
N = int(input())


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


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


use_list = []
cnt = 0
while True:
    flag = 0
    div_list = make_divisors(N)
    if len(div_list) == 1:
        break
    for i in range(1, len(div_list)):
        if len(collections.Counter(prime_factorize(div_list[i]))) == 1 and div_list[i] not in use_list:
            use_list.append(div_list[i])
            N = N // div_list[i]
            cnt += 1
            flag = 1
            break
    if flag == 0:
        break
print(cnt)

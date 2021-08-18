N = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


L1 = factorization(N - 1)
s = 1
for [a, b] in L1:
    s *= (b + 1)


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


for i in set(make_divisors(N)) - {1}:
    temp = N
    while temp % i == 0:
        temp //= i
    if (temp - 1) % i == 0:
        s += 1
s -= 1
if N == 2:
    print(1)
else:
    print(s)

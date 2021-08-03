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

tmp = n - 1
ret = len(make_divisors(tmp)) - 1

tmplen = make_divisors(n)

for item in tmplen:
    if item == 1:
        continue
    val = n
    while True:
        if val % item == 0:
            val = val // item
        else:
            if val % item == 1:
                ret += 1
            break

print(ret)

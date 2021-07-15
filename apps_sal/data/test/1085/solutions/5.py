import copy

# 約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 2
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1] + [n]

# 素因数分解
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


n = int(input())
if n == 2:
    print(1)
    return

div1 = make_divisors(n-1)
cnt = len(div1)

div2 = make_divisors(n)


for i in div2:
    x = copy.deepcopy(n)
    while x >= i:
        if x % i == 0:
            x //= i
        else:
            break
    if x == 1 or x % i == 1:
        cnt += 1

print(cnt)

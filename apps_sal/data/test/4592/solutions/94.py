def factorize(n):
    # https://python.ms/factorize/#%E5%AE%9F%E8%A3%85
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append([b, e])
        b, e = b + 1, 0
    if n > 1:
        fct.append([n, 1])
    return fct


n = int(input())

num = 1
for i in range(1, n + 1):
    num *= i

fact = factorize(num)
# print(fact)
ans = 1
for i in range(len(fact)):
    ans *= (fact[i][1] + 1)

print(ans % (10**9 + 7))

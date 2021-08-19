def factorial_1(n: int):
    for i in range(2, n + 1):
        if i > n ** 0.5:
            return n
        elif n % i == 0:
            return i


def factorial_2(n: int):
    res = dict()
    while n > 1:
        f_now = factorial_1(n)
        n //= f_now
        res[f_now] = res.get(f_now, 0) + 1
    return res


(n, k) = map(int, input().split())
(f_k, x) = (factorial_2(k), float('inf'))
for (key, val) in f_k.items():
    (qua_f, pow_) = (0, key)
    while pow_ <= n:
        qua_f += n // pow_
        pow_ *= key
    x = min(x, qua_f // val)
print(x)

(a, b) = map(int, input().split())


def factorization(n):
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


s_a = set(factorization(a))
s_b = set(factorization(b))
ans_arr = s_a & s_b
print(len(ans_arr) + 1)

def factorize(n):
    fct = set()
    (b, e) = (2, 0)
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e > 0:
            fct.add(b)
        (b, e) = (b + 1, 0)
    if n > 1:
        fct.add(n)
    return fct


(a, b) = map(int, input().split())
print(len(factorize(a) & factorize(b)) + 1)

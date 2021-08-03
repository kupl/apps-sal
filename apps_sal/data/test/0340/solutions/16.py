def factor(n):

    def factor_n(m):
        for q in range(2, m + 1):
            if m % q == 0:
                return q
            if q > m**(1 / 2):
                return m

    factors = {}
    while True:
        factor_naw = factor_n(n)
        n //= factor_naw
        factors[factor_naw] = factors.get(factor_naw, 0) + 1
        if n == 1:
            break
    return factors


n = int(input())
if n == 1:
    print(n, 0)
else:
    a = factor(n)
    s = max(a.values())
    if s == 1:
        print(n, 0)
    else:
        q1, q2 = 1, 0
        while q1 < s:
            q1 *= 2
            q2 += 1
        answer = 1
        for q in a:
            answer *= q
        p = set(a.values())
        print(answer, q2 + 1 if len(set(a.values())) != 1 or 2**q2 != s else q2)

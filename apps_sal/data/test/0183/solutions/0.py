n, k, m = list(map(int, input().split()))
d, r, p, P = 0, 0, 1 % k, (10**(n - 1)) * 9
F = [0] * k
F[0] = 1
while d < n:
    d += 1
    P //= 10
    E = [0] * k
    if P == 0:
        P = 1
    i = 1
    while i < 10:
        j = (-i * p) % k
        f = 0
        while f < k:
            E[f] += F[j]
            f += 1
            j += 1
            if j == k:
                j = 0
        i += 1
    r += E[0] * P
    p = p * 10 % k
    E[0] = 0
    i = 1
    while i < k:
        F[i] = (F[i] + E[i]) % m
        i += 1
    F[0] = 1
print(r % m)
"""
3 6 9
13 16 19	12 15 18
23 26 29	21 24 27
33 36 39	30
43 46 49	42 45 48
53 56 59	51 54 57
63 66 69	60
73 76 79	72 75 78
83 86 89	81 84 87
93 96 99	90
"""

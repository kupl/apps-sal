(n, k, m) = list(map(int, input().split()))
(d, r, p, P) = (0, 0, 1 % k, 10 ** (n - 1) * 9)
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
        j = -i * p % k
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
'\n3 6 9\n13 16 19\t12 15 18\n23 26 29\t21 24 27\n33 36 39\t30\n43 46 49\t42 45 48\n53 56 59\t51 54 57\n63 66 69\t60\n73 76 79\t72 75 78\n83 86 89\t81 84 87\n93 96 99\t90\n'

mod = 10 ** 9 + 7
(N, aa, ab, ba, bb) = open(0).read().split()
N = int(N)
if N <= 3 or aa == ab == 'A' or ab == bb == 'B':
    print(1)
elif aa + ab + ba == 'BAB' or ab + ba + bb == 'BAA':
    print(pow(2, N - 3, mod))
else:
    (a, b) = (1, 1)
    for _ in range(N - 3):
        (a, b) = (a + b, a)
    print(a % mod)

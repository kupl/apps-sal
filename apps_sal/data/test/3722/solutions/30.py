(N, *S) = open(0).read().split()
N = int(N)
S = ''.join(S)
mod = 10 ** 9 + 7
if N == 2:
    print(1)
elif S in ['ABAA', 'BABA', 'BABB', 'BBAA']:
    print(pow(2, N - 3, mod))
elif S in ['ABBA', 'BAAA', 'BAAB', 'BBBA']:
    a = b = 1
    for _ in range(N - 3):
        (a, b) = (b, a + b)
        a %= mod
        b %= mod
    print(b)
else:
    print(1)

N, M = map(int, input().split())

x = abs(N - M)
if x >= 2:
    print(0)
else:
    mod = 10**9 + 7
    a = 1
    for i in range(2, N + 1):
        a *= i
        a %= mod
    b = 1
    for i in range(2, M + 1):
        b *= i
        b %= mod

    if x == 0:
        print(a * b * 2 % mod)
    else:
        print(a * b % mod)

(N, M) = map(int, input().split())
gcd = M // N
while gcd * N != M:
    gcd = M // N
    N = 1 + (M - 1) // gcd
print(gcd)

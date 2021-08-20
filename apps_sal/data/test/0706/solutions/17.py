M = 1000000007
(A, B, n, x) = (int(x) for x in input().split())
if A > 1:
    An = pow(A, n, M)
    print((An * x % M + B * (1 - An) * pow(1 - A, M - 2, M) % M) % M)
else:
    print((x + B * n) % M)

M = int(1e9 + 7)
A, B, n, x = (int(x) for x in input().split())
if A > 1:
    An = pow(A, n, M)
    print((An * x + B * (1-An) * pow(1-A, M-2, M)) % M)
else:
    print((x + B*n) % M)


P, M, A, I = input, max, int, -10**9
n, a = A(P()), list(map(A, P().split()))
x, y, z = 0, I, I
for i, L in enumerate(a):
    if i % 2:
        z = M(y, z)
        y += L
    else:
        y = M(x, y)
        x += L
        z += L
print(M(y, z)if n % 2else M(x, y))

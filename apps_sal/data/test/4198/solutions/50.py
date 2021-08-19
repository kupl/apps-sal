(A, B, X) = [int(_) for _ in input().split()]


def d(N):
    return len(str(N))


nmin = 0
nmax = 10 ** 9
while nmax - nmin > 1:
    n = (nmin + nmax) // 2
    if A * n + B * d(n) <= X:
        nmin = n
    else:
        nmax = n
if A * nmax + B * d(nmax) <= X:
    print(nmax)
else:
    print(nmin)

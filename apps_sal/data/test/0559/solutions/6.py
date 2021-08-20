def solve():
    p = int(input())
    (*A,) = map(int, input().split())
    L = p - 1
    fact = [1] * (L + 1)
    rfact = [1] * (L + 1)
    r = 1
    for i in range(1, L + 1):
        fact[i] = r = r * i % p
    rfact[L] = r = pow(r, p - 2, p)
    for i in range(L, 0, -1):
        rfact[i - 1] = r = r * i % p
    V = [-fact[p - 1] * rfact[k] * rfact[p - 1 - k] % p for k in range(p)]
    B = [-i for i in range(p)]
    R = [0] * p
    I = [i for (i, a) in enumerate(A) if a]
    C = [a for a in A]
    for k in range(p):
        r = 0
        R[k] = V[k] * sum(C) % p
        for i in I:
            C[i] = C[i] * B[i] % p
    R[-1] += len(I)
    for k in range(p):
        R[k] %= p
    R.reverse()
    print(*R)


solve()

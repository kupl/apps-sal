(N, K, *L) = map(int, open(0).read().split())
L = L[::-1]
I = set()
X = 0
U = []
D = []
for (d, t) in sorted(zip(*[iter(L)] * 2))[::-1]:
    if t in I:
        D += (d,)
    elif X < K:
        I |= {t}
        U += (d,)
        X += 1
D += (0,)
i = K - X
while X and U[-1] + 2 * X - 1 <= D[i]:
    U.pop()
    X -= 1
    i += 1
print(sum(U + D[:i]) + X ** 2)

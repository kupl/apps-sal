from scipy.special import comb
import sys
readline = sys.stdin.readline

N, A, B = list(map(int, readline().split()))
V = list(map(int, readline().split()))


V = sorted(V, reverse=True)

print((sum(V[:A]) / A))


P = V[A - 1]
pcnt = V.count(P)

if V[0] == P:
    ans = 0
    for i in range(A, B + 1):
        ans += comb(pcnt, i, exact=True)
    print(ans)
else:
    pneed = (V[:A]).count(P)
    print((comb(pcnt, pneed, exact=True)))

import itertools
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return list(map(int, sys.stdin.readline().split()))
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]


N, *A = mi()
L = [ii() for _ in range(N)]
L_ = [L[i] for i in range(N)]
N_ = N

A = sorted(A)
tmp = [0] * 3
ans = float('inf')

for k in itertools.product([0, 1], repeat=N_):
    N = sum(k)
    if N < 3:
        continue
    L = []
    for x in range(N_):
        if k[x]:
            L.append(L_[x] * k[x])
    sum_l = sum(L)

    for i in range(1, N + 1):
        for koho_i in range(1, 2**i):
            for koho_j in range(1, 2**i):
                j = i
                if koho_i & koho_j:
                    continue
                tmp[0] = sum([L[x] * min((koho_i & 1 << x), 1) for x in range(i)])
                tmp[1] = sum([L[x] * min((koho_j & 1 << x), 1) for x in range(j)])
                tmp[2] = sum_l - tmp[0] - tmp[1]

                if 0 in tmp:
                    continue

                tmp = sorted(tmp)
                cost = (N - 3) * 10 + sum([abs(tmp[x] - A[x]) for x in range(3)])
                ans = min(ans, cost)

print(ans)

import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline
(l, r) = [int(i) for i in readline().split()]


def make_dp(init, size):
    res = '[{}]*{}'.format(init, size[-1])
    for i in reversed(size[:-1]):
        res = '[{} for _ in [0]*{}]'.format(res, i)
    return eval(res)


MOD = 10 ** 9 + 7
R = bin(r)[2:]
L = bin(l)[2:]
L = '0' * (len(R) - len(L)) + L
dp = make_dp(0, (len(R) + 1, 2, 2, 2))
dp[0][0][0][0] = 1
for (i, (r, l)) in enumerate(zip(R, L)):
    ri = int(r)
    li = int(l)
    for is_less in range(2):
        for is_more in range(2):
            for is_nonzero in range(2):
                for dl in range(0 if is_more else li, 2):
                    for dr in range(dl, 2 if is_less else ri + 1):
                        dp[i + 1][is_nonzero or dr != 0][is_more or li < dl][is_less or dr < ri] += dp[i][is_nonzero][is_more][is_less] * (dr == dl or is_nonzero)
                        dp[i + 1][is_nonzero or dr != 0][is_more or li < dl][is_less or dr < ri] %= MOD
ans = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            ans += dp[-1][i][j][k]
print(ans % MOD)

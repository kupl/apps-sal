import sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    import os
    import re
    with open(__file__) as f:
        source = f.read().split('###''nbacl')
    for s in source[1:]:
        s = re.sub("'''.*", '', s)
        sp = s.split(maxsplit=1)
        if os.path.dirname(sp[0]):
            os.makedirs(os.path.dirname(sp[0]), exist_ok=True)
        with open(sp[0], 'w') as f:
            f.write(sp[1])
    from nbmodule import cc
    cc.compile()
from nbmodule import solve

N, M = [int(x) for x in input().split()]
ans = solve(N, M)
print(ans)
'''
###nbacl nbmodule.py
import numpy as np
from numpy import int64
from numba import njit
from numba.types import i8
from numba.pycc import CC

cc = CC('nbmodule')
MOD = 1000000007


@njit
def inv_mod(x, mod):
    old_t, t = 0, 1
    old_r, r = mod, x

    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_t, t = t, old_t - quotient * t

    return old_t % mod


@njit
def calc_fac(fac):
    fac[0] = 1
    for i in range(1, fac.shape[0]):
        fac[i] = fac[i - 1] * i % MOD


@njit
def calc_inv_fac(inv_fac):
    inv_fac[0] = 1
    for i in range(1, inv_fac.shape[0]):
        inv_fac[i] = inv_fac[i - 1] * inv_mod(i, MOD) % MOD


@njit((i8, i8), cache=True)
@cc.export('solve', (i8, i8))
def solve(N, M):
    fac = np.empty(M + 1, dtype=int64)
    inv_fac = np.empty(M + 1, dtype=int64)

    def p(m, n):
        return fac[m] * inv_fac[m - n] % MOD
    def c(m, n):
        return fac[m] * inv_fac[n] % MOD * inv_fac[m - n] % MOD

    calc_fac(fac)
    calc_inv_fac(inv_fac)

    ret = 0
    for r in range(N + 1):
        if r & 1:
            ret = (ret - c(N, r) * p(M - r, N - r)) % MOD
        else:
            ret = (ret + c(N, r) * p(M - r, N - r)) % MOD
    return ret * p(M, N) % MOD


def __starting_point():
    cc.compile()

'''

__starting_point()

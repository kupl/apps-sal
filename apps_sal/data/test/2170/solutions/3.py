import sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    import os
    import re
    with open(__file__) as f:
        source = f.read().split('###nbacl')
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
(N, M) = [int(x) for x in input().split()]
ans = solve(N, M)
print(ans)
"\n###nbacl nbmodule.py\nimport numpy as np\nfrom numpy import int64\nfrom numba import njit\nfrom numba.types import i8\nfrom numba.pycc import CC\n\ncc = CC('nbmodule')\nMOD = 1000000007\n\n\n@njit\ndef inv_mod(x, mod):\n    old_t, t = 0, 1\n    old_r, r = mod, x\n\n    while r != 0:\n        quotient = old_r // r\n\n        old_r, r = r, old_r - quotient * r\n        old_t, t = t, old_t - quotient * t\n\n    return old_t % mod\n\n\n@njit\ndef calc_fac(fac):\n    fac[0] = 1\n    for i in range(1, fac.shape[0]):\n        fac[i] = fac[i - 1] * i % MOD\n\n\n@njit\ndef calc_inv_fac(inv_fac):\n    inv_fac[0] = 1\n    for i in range(1, inv_fac.shape[0]):\n        inv_fac[i] = inv_fac[i - 1] * inv_mod(i, MOD) % MOD\n\n\n@njit((i8, i8), cache=True)\n@cc.export('solve', (i8, i8))\ndef solve(N, M):\n    fac = np.empty(M + 1, dtype=int64)\n    inv_fac = np.empty(M + 1, dtype=int64)\n\n    def p(m, n):\n        return fac[m] * inv_fac[m - n] % MOD\n    def c(m, n):\n        return fac[m] * inv_fac[n] % MOD * inv_fac[m - n] % MOD\n\n    calc_fac(fac)\n    calc_inv_fac(inv_fac)\n\n    ret = 0\n    for r in range(N + 1):\n        if r & 1:\n            ret = (ret - c(N, r) * p(M - r, N - r)) % MOD\n        else:\n            ret = (ret + c(N, r) * p(M - r, N - r)) % MOD\n    return ret * p(M, N) % MOD\n\n\ndef __starting_point():\n    cc.compile()\n\n"
__starting_point()

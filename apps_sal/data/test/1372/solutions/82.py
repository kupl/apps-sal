import sys
import numpy as np


def numba_compile(numba_config):
    import os
    import sys
    if sys.argv[-1] == 'ONLINE_JUDGE':
        from numba import njit
        from numba.pycc import CC
        cc = CC('my_module')
        for (func, signature) in numba_config:
            vars()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        return
    elif os.name == 'posix':
        exec(f"from my_module import {','.join((func.__name__ for (func, _) in numba_config))}")
        for (func, _) in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for (func, signature) in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print('compiled!', file=sys.stderr)


def solve(H, N, AB):
    dp = np.empty(H + 1, dtype=np.int64)
    dp[:] = 1 << 60
    dp[0] = 0
    for n in range(1, N + 1):
        (a, b) = AB[n - 1]
        for h in range(H):
            dp[min(H, h + a)] = min(dp[min(H, h + a)], dp[h] + b)
    return dp[-1]


numba_compile([[solve, 'i8(i8,i8,i8[:,:])']])


def main():
    (H, N) = map(int, input().split())
    AB = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(N, 2)
    ans = solve(H, N, AB)
    print(ans)


main()

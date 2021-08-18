# AOTコンパイルテスト
import sys


def solve(n):
    su = 0
    for i in range(1, n + 1):
        m = n // i
        su += m * (2 * i + (m - 1) * i) // 2
    return su


if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', '(i8)')(solve)
    cc.compile()
    return

n = int(input())
print(solve(n))

import sys

def solve():
    N = int(input())
    mod = 7 + 10 ** 9
    total = pow(10, N, mod)
    noZeroOrNine = pow(9, N, mod)
    noZeroAndNine = pow(8, N, mod)
    print((total - 2 * noZeroOrNine + noZeroAndNine) % mod)


    return 

def __starting_point():
    solve()
__starting_point()

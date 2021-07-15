import sys
from itertools import accumulate

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    n, k = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    sumB = sum(B)
    dif = [a - b for a, b in zip(A, B)]
    dif.sort()
    dif = [0] + list(accumulate(dif))

    ans = float('inf')

    for i in range(k, n + 1):
        ans = min(ans, sumB + dif[i])

    print(ans)
    

def __starting_point():
    solve()
__starting_point()

import sys
import copy
from collections import Counter


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def solve():
    n = int(input())
    Sn = list(map(int, input()))
    Mn = list(map(int, input()))
    # debug(Sn, locals())

    cntM1 = Counter(Mn)
    cntM2 = copy.deepcopy(cntM1)
    # debug(cntM, locals())

    # max-win
    maxwin = 0
    for d in Sn:
        for a in range(d + 1, 10):
            if cntM1[a] > 0:
                cntM1[a] -= 1
                maxwin += 1
                break
        else:
            for a in range(0, d + 1):
                if cntM1[a] > 0:
                    cntM1[a] -= 1
                    break

    # min-lose
    minlose = 0
    for d in Sn:
        for a in range(d, 10):
            if cntM2[a] > 0:
                cntM2[a] -= 1
                break
        else:
            for a in range(0, d):
                if cntM2[a] > 0:
                    minlose += 1
                    cntM2[a] -= 1
                    break

    print(minlose)
    print(maxwin)


def __starting_point():
    solve()


__starting_point()

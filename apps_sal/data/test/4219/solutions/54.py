import sys
from io import StringIO
import unittest
import itertools


def yn(b):
    print("Yes" if b == 1 else "No")
    return


def resolve():
    readline = sys.stdin.readline
    n = int(readline())
    dat = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        m = int(readline())
        for j in range(m):
            x, y = map(int, readline().rstrip().split())
            x -= 1
            dat[i][x] = y

    ans = 0
    for ptn in itertools.product([False, True], repeat=n):
        ok = True
        for i in range(n):
            if ptn[i] == False:
                continue
            for j in range(n):
                if dat[i][j] == -1:
                    continue
                if dat[i][j] == 1 and ptn[j] == False:
                    ok = False
                    break
                if dat[i][j] == 0 and ptn[j] == True:
                    ok = False
                    break
            if ok == False:
                break
        if ok == True:
            ans = max(ans, ptn.count(True))
    print(ans)

    return


if 'doTest' not in globals():
    resolve()
    return

import logging
import sys
from inspect import currentframe
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
logging.basicConfig(level=logging.DEBUG)


def dbg(*args):
    id2names = {id(v): k for (k, v) in list(currentframe().f_back.f_locals.items())}
    logging.debug(', '.join((id2names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args)))


def solve(n, t):
    s = '110'
    num = 10000000000.0
    if t == '0':
        return num
    elif t == '1':
        return 2 * num
    ans = 0
    for i in range(3):
        num110 = (len(t) + i + 2) // 3
        ok = True
        for j in range(len(t)):
            if t[j] != s[(i + j) % 3]:
                ok = False
        if ok:
            ans += num - num110 + 1
    return ans


def main():
    n = int(input())
    t = input()
    dbg(len(t))
    t = t.strip()
    dbg(len(t))
    print(int(solve(n, t)))


def __starting_point():
    main()


__starting_point()

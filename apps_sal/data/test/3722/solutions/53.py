from collections import Counter, defaultdict
import sys
import math
from functools import cmp_to_key
from itertools import permutations

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)


def solve(n, caa, cab, cba, cbb):
    s_list = {'AB'}
    for i in range(n - 2):
        tmp = set()
        for s in s_list:
            for i in range(len(s) - 1):
                if s[i:i + 2] == 'AA':
                    tmp.add(s[:i + 2] + caa + s[i + 2:])
                if s[i:i + 2] == 'AB':
                    tmp.add(s[:i + 2] + cab + s[i + 2:])
                if s[i:i + 2] == 'BA':
                    tmp.add(s[:i + 2] + cba + s[i + 2:])
                if s[i:i + 2] == 'BB':
                    tmp.add(s[:i + 2] + cbb + s[i + 2:])
        s_list = tmp
    print(("{}\t{}".format(n, len(s_list))))


def main():
    n = int(input())
    caa, cab, cba, cbb = input(), input(), input(), input()
    if n <= 3:
        print((1))
        return
    if cab == 'A':
        if caa == 'B':
            if cba == cab:
                p = 1
                pp = 1
                for i in range(3, n):
                    v = (p + pp) % mod
                    pp, p = p, v
                print(p)
            else:
                print((pow(2, n - 3, mod)))
        else:
            print((1))
    else:
        if cbb == 'A':
            if cba == cab:
                p = 1
                pp = 1
                for i in range(3, n):
                    v = (p + pp) % mod
                    pp, p = p, v
                print(p)
            else:
                print((pow(2, n - 3, mod)))
        else:
            print((1))


main()

from inspect import currentframe
import sys
import os
import time
import re
from pydoc import help
import string
import math
from operator import itemgetter
from collections import Counter
from collections import deque
from collections import defaultdict as dd
import fractions
from heapq import heappop, heappush, heapify
import array
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy as dcopy
import itertools
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
GOSA = 1.0 / 10 ** 10
MOD = 10 ** 9 + 7
ALPHABETS = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def DP(N, M, first):
    return [[first] * M for n in range(N)]


def DP3(N, M, L, first):
    return [[[first] * L for n in range(M)] for _ in range(N)]


def dump(*args):
    names = {id(v): k for (k, v) in currentframe().f_back.f_locals.items()}
    print(', '.join((names.get(id(arg), '???') + ' => ' + repr(arg) for arg in args)), file=sys.stderr)


def local_input():
    from pcm.utils import set_stdin
    import sys
    from pathlib import Path
    parentdir = Path(os.path.dirname(__file__)).parent
    inputfile = parentdir.joinpath('test/sample-1.in')
    if len(sys.argv) == 1:
        set_stdin(inputfile)


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    m = max(A)
    res = 0
    c = 0
    for a in A:
        if a == m:
            c += 1
            res = max(res, c)
        else:
            c = 0
    print(res)
    return 0


def __starting_point():
    try:
        local_input()
    except:
        pass
    solve()


__starting_point()

from bisect import bisect_left
from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(200000)


def read():
    S = input().strip()
    T = input().strip()
    return S, T


def have_ahswer(S, T):
    cs = Counter(S)
    ct = Counter(T)
    for k in list(ct.keys()):
        if cs[k] == 0:
            return False
    return True


def solve(S, T):
    Z = "abcdefghijklmnopqrstuvwxyz"
    if not have_ahswer(S, T):
        return -1
    D = defaultdict(list)
    for i, s in enumerate(S):
        D[s].append(i)
    ans = 0
    prev_index = -1
    N = len(S)
    for t in T:
        a = D[t]
        i = bisect_left(a, prev_index + 1)
        if i < len(a):
            next_index = a[i]
            ans += next_index - prev_index
        else:
            next_index = a[0]
            ans += N + next_index - prev_index
        prev_index = next_index
    return ans


def __starting_point():
    inputs = read()
    print(("{}".format(solve(*inputs))))


__starting_point()

import sys
from itertools import accumulate
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, k) = list(map(int, input().split()))
    A = list([int(x) - 1 for x in input().split()])
    S = [0] + list(accumulate(A))
    S = [s % k for s in S]
    cnt = defaultdict(int)
    res = 0
    for i in range(n + 1):
        if i >= k:
            cnt[S[i - k]] -= 1
        res += cnt[S[i]]
        cnt[S[i]] += 1
    print(res)


def __starting_point():
    resolve()


__starting_point()

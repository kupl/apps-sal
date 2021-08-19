from functools import reduce
from operator import mul
from collections import Counter


def solve():
    N = int(input())
    S = input()
    ret = 0
    RGB_ = {'R': 0, 'G': 0, 'B': 0}
    counter = Counter(S)
    for k, v in counter.items():
        RGB_[k] += v
    ret = reduce(mul, RGB_.values())

    # print(ret)
    RGB_mergin_len = 0
    # R.{l}G.{l}B を引く
    while 3 + RGB_mergin_len * 2 <= N:
        for i in range(N - (3 + RGB_mergin_len * 2) + 1):
            j = i + 1 + RGB_mergin_len
            k = i + 2 + 2 * RGB_mergin_len
            if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                ret -= 1

            # print(i, j, k)
            # print(S[i], S[j], S[k], ret)
        RGB_mergin_len += 1

    print(ret)


solve()

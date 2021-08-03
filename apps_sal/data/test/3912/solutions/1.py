# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/10/22 18:15

"""

N = int(input())
S = input()


def split(s, wc, pl, n):

    ans = []

    if pl % 2 == 0:
        if any([x % 2 == 1 for x in list(wc.values())]):
            return []
        for i in range(0, len(s), pl):
            t = s[i:i + pl]
            ans.append(t[::2] + t[::-1][::2])

        return ans

    mid = [w for w, c in list(wc.items()) if c % 2 == 1]

    if len(mid) > n:
        return []

    midindex = 0
    while len(ans) < n:
        t = ''
        u = mid[midindex] if midindex < len(mid) else ''
        midindex += 1
        if not u:
            u = list([w for w, c in list(wc.items()) if c > 0])[0]
        wc[u] -= 1

        need = pl - 1
        while need > 0:
            pneed = need
            for w, c in [(w, c) for w, c in list(wc.items())]:
                if c > need:
                    t += str(w) * (need // 2)
                    wc[w] -= need
                    need = 0
                    break
                elif c > 1:
                    c //= 2
                    t += str(w) * c
                    wc[w] -= c * 2
                    need -= c * 2
            if need == pneed:
                return []
        t = t + u + t[::-1]
        if len(t) < pl:
            return []
        ans.append(t)

    return ans


S = "".join(sorted(list(S)))
WC = collections.Counter(S)

for parts in range(1, N + 1):
    if N % parts == 0:
        wc = {k: v for k, v in list(WC.items())}
        ans = split(S, wc, N // parts, parts)
        if ans:
            print(parts)
            print(" ".join(ans))
            return

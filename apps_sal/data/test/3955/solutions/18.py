
"""

created by shuangquan.huang at 1/10/20

a simple conclusion is that we should multiple only one v with x K times

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, X, A):
    prefix = [0 for _ in range(N)]
    suffix = [0 for _ in range(N)]

    for i, v in enumerate(A):
        prefix[i] = (prefix[i - 1] if i - 1 >= 0 else 0) | v
    for i in range(N - 1, -1, -1):
        suffix[i] = (suffix[i + 1] if i + 1 < N else 0) | A[i]

    ans = 0
    for i, v in enumerate(A):
        a = prefix[i - 1] if i - 1 >= 0 else 0
        b = suffix[i + 1] if i + 1 < N else 0
        ans = max(ans, a | b | (v * X**K))

    return ans


N, K, X = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, K, X, A))

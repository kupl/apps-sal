import math
import random
import string
from functools import lru_cache
from operator import truediv
from typing import List, Set
import collections
import functools
import heapq
import itertools
import sys
from functools import lru_cache
from typing import List
import numpy as np
import collections
import functools
import heapq
import itertools
import sys
from functools import lru_cache
from typing import List

'''
53. Maximum Subarray 无循环
    dp[i] = max(A[i], dp[i-1] + A[i])
    显然当dp[i-1] < 0 时， dp[i] = A[i]，则有：
    dp[i] = A[i] + max(dp[i-1], 0)

类比53，此题加了循环。也就是找到尾部和开头的最大正数组。

https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

但其实就是找到中间的最负子数组。
'''


class Solution:
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


# r = Solution()
# a = r.maxSubarraySumCircular([3,-1,2,-1])
# print(a)

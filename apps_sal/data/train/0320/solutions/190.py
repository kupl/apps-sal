from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from typing import List
import itertools
import math
import heapq
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        cc = Counter(nums)
        while True:
            dup = defaultdict(int)
            do_even = False
            for n in cc:
                if n == 0:
                    continue
                if n % 2:
                    cnt += cc[n]
                    if n - 1 > 0:
                        do_even = True
                        dup[n // 2] += cc[n]
                else:
                    do_even = True
                    dup[n // 2] += cc[n]
            if do_even:
                cnt += 1
            if not dup:
                return cnt
            cc = dup

        return cnt


sol = Solution()

nums = [1, 5]
nums = [2, 2]
nums = [4, 2, 5]

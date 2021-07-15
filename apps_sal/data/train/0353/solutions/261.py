import math
import random
import string
from functools import lru_cache
from operator import truediv
from typing import List
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
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

普通思路：排序。分别计算各个区间
3 -> 1
3 5 -> 2^0 在或不在
3 5 6 -> 2^1
3 5 6 7 -> 2^2

加强，与其每次计算，不如到最后一个才计算，因为：
1 + 2^0 + 2^1 + 2^2 = 2^3

可以用二分加速寻找。

终极优化：对比二分或者for循环找最后一个，实际上还是做了大量重复的比较。

根据+法的特点进行双端优化，大于target则右侧减一，小于target则左侧加一。
'''


class Solution:
    def numSubseqNormal(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            for j in range(i, n):
                if (nums[i] + nums[j]) <= target:
                    if i == j:
                        count += 1
                    else:
                        count += pow(2, j - i - 1)
                    count %= mod
        return count

    # 加强
    def numSubseq1(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            j = i
            while j < n and (nums[i] + nums[j]) <= target:
                j += 1
            if i == j:
                if (nums[i] + nums[j]) <= target:
                    count += 1
            elif (nums[i] + nums[j - 1]) <= target:  # 防止第一个数就超过
                count += pow(2, j - i - 1) % mod
        return count % mod

    def findLast(self, nums, start, end, target):
        first = nums[start]
        while start <= end:
            mid = int((start + end) / 2)
            second = nums[mid]
            if first + second > target:
                end = mid - 1
            elif first + second < target:
                start = start + 1
            elif first + second == target:
                start = start + 1
        return start

    def numSubseq12(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        mod = 10 ** 9 + 7
        pow_map = [1 for _ in range(n)]
        for i in range(1, n):
            pow_map[i] = (2 * pow_map[i - 1]) % mod

        for i in range(n):
            if nums[i] > target:
                    break
            j = self.findLast(nums, i, n - 1, target)
            if i == j:
                if (nums[i] + nums[j]) <= target:
                    count += 1
            elif (nums[i] + nums[j - 1]) <= target:  # 防止第一个数就超过
                count += pow_map[j - i - 1]
        return count % mod

    # 双端优化
    def numSubseq(self, A, target):
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod

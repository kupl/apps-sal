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
反转K个位置的0为1，问最长连续1的长度。

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


思路：滑动窗口。
主要思想，开区间伸缩左右边界。闭区间不好处理初始情况。

'''


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # 开区间[start, end)
        start = 0
        end = 0
        ret = 0
        while end < len(A):
            if A[end] == 1:
                end += 1
            else:
                if K > 0:
                    end += 1
                    K -= 1
                else:
                    if A[start] == 0:
                        K += 1
                    start += 1
            ret = max(ret, end - start)
        return ret


# A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# K = 3
#
# r = Solution()
# a = r.longestOnes(A, K)
# print(a)

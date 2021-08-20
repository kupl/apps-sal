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
'\n反转K个位置的0为1，问最长连续1的长度。\n\nInput: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3\nOutput: 10\nExplanation: \n[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]\nBolded numbers were flipped from 0 to 1.  The longest subarray is underlined.\n\n\n思路：滑动窗口。\n主要思想，开区间伸缩左右边界。闭区间不好处理初始情况。\n\n'


class Solution:

    def longestOnes1(self, A: List[int], K: int) -> int:
        start = 0
        end = 0
        ret = 0
        while end < len(A):
            if A[end] == 1:
                end += 1
            elif K > 0:
                end += 1
                K -= 1
            else:
                if A[start] == 0:
                    K += 1
                start += 1
            ret = max(ret, end - start)
        return ret

    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1

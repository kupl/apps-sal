from collections import *
from functools import *
import numpy as np
from typing import *


class Solution:
    def maxJumps(self, nums: List[int], d: int) -> int:
        N = len(nums)
        left_jumps = [[] for _ in range(N)]
        left = [(-1, np.inf)]
        for i in range(N):
            while left[-1][1] < nums[i]:
                j, _ = left.pop()
                if abs(j - i) <= d:
                    left_jumps[i].append(j)
            left.append((i, nums[i]))
        
        right_jumps = [[] for _ in range(N)]
        right = [(-1, np.inf)]
        for i in reversed(range(N)):
            while right[-1][1] < nums[i]:
                j, _ = right.pop()
                if abs(j - i) <= d:
                    right_jumps[i].append(j)
            right.append((i, nums[i]))
        
        @lru_cache(maxsize=None)
        def longest_path_from(pos: int):
            left_max = max((longest_path_from(p) for p in left_jumps[pos]), default=0)
            right_max = max((longest_path_from(p) for p in right_jumps[pos]), default=0)
            return max(1 + left_max, 1 + right_max)

        return max(longest_path_from(i) for i in range(N))

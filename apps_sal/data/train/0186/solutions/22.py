from typing import List
import numpy
import functools


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        cache = {}

        def solve(remaining):
            if not remaining:
                return ''
            if remaining in cache:
                return cache[remaining]
            maxium = '0'
            for i in range(len(cost)):
                if cost[i] > remaining:
                    continue
                result = solve(remaining - cost[i])
                if result == '0':
                    continue
                maxium = larger(maxium, str(i + 1) + result)
                pass
            cache[remaining] = maxium
            return maxium
            pass

        def larger(a, b):
            if len(a) > len(b):
                return a
            if len(a) < len(b):
                return b
            return max(a, b)
        return solve(target)

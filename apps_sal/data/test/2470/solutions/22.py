import bisect
from typing import List
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        array = arr1
        replace = list(sorted(set(arr2)))

        @lru_cache(None)
        def dfs(array_pos: int, prev_number: int) -> int:
            min_replacements = len(replace) * 2

            if array_pos == len(array):
                return 0

            next_replace_pos = 0

            if array_pos > 0:
                next_replace_pos = bisect.bisect(replace, array[array_pos - 1])

            if array_pos == 0 or (
                next_replace_pos < len(replace)
            ):
                tmp = array[array_pos]
                array[array_pos] = replace[next_replace_pos]
                min_replacements = min(min_replacements, dfs(array_pos + 1, array[array_pos]) + 1)
                array[array_pos] = tmp

            if array_pos == 0 or array[array_pos - 1] < array[array_pos]:
                min_replacements = min(min_replacements, dfs(array_pos + 1, array[array_pos]))

            return min_replacements

        result = dfs(0, -100)

        if result > len(replace):
            return -1

        return result

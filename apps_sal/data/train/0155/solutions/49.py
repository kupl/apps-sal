import functools


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:

        @functools.lru_cache(None)
        def check_i(inow):
            max_son = 0
            for i in range(1, min(d + 1, len(arr) - inow)):
                if arr[inow + i] >= arr[inow]:
                    break
                max_son = max(max_son, check_i(inow + i))
            for i in range(1, min(d + 1, inow + 1)):
                if arr[inow - i] >= arr[inow]:
                    break
                max_son = max(max_son, check_i(inow - i))
            return max_son + 1
        return max([check_i(i) for i in range(len(arr))])

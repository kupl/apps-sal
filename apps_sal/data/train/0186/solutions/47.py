from functools import lru_cache


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:

        @lru_cache(None)
        def dp(index, remain):
            if remain == 0:
                return ''
            elif remain < 0 or index > len(cost):
                return '0'
            take = str(index) + dp(1, remain - cost[index - 1])
            skip = dp(index + 1, remain)
            return get_bigger(take, skip)

        def get_bigger(a, b):
            if '0' in a:
                return b
            elif '0' in b:
                return a
            elif int(a) > int(b):
                return a
            else:
                return b
        ans = dp(1, target)
        return ans if '0' not in ans else '0'

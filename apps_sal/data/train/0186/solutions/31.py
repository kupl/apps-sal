class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        @lru_cache(None)
        def rec(rem):
            if rem <= 0:
                return 0 if rem == 0 else -math.inf

            ans = -math.inf
            for c in cost:
                ans = max(ans, rec(rem - c) + 1)
            return ans

        ln = rec(target)
        if ln <= 0:
            return '0'

        def path(rem, now):
            # print(rem, now)
            if rem <= 0:
                return now if rem == 0 else ''
            for i, c in enumerate(reversed(cost)):
                if rec(rem - c) + 1 == rec(rem):
                    return path(rem - c, now + str(9 - i))
            return ''

        ans = path(target, '')
        print(ans)
        return ans

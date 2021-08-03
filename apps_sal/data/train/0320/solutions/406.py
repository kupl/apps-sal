class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def steps(n):
            if n == 0:
                return 0, 0, 0
            if n == 1:
                return 1, 1, 0
            if n & 1:
                a, b, c = steps(n - 1)
                return a + 1, b + 1, c

            a, b, c = steps(n // 2)
            return a + 1, b, c + 1

        # print(steps(5))
        evens = 0
        odds = 0
        for num in nums:
            a, b, c = steps(num)
            odds += b
            # print(num, a,b,c)
            evens = max(evens, c)

        return odds + evens

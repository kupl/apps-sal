class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(maxsize=None)
        def get_power(n):
            if n == 1:
                return 0
            elif n % 2:
                return 1 + get_power(3 * n + 1)
            return 1 + get_power(n // 2)

        nums = []

        for i in range(lo, hi + 1):
            nums.append([get_power(i), i])

        nums.sort()

        return nums[k - 1][1]

class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def distance(n):
            if n == 1:
                return 0
            new_n = n // 2 if n % 2 == 0 else n * 3 + 1
            return 1 + distance(new_n)
        nums = list(range(lo, hi + 1))
        nums.sort(key=lambda x: (distance(x), x))
        return nums[k - 1]

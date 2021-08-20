class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def power(n: int):
            step = 0
            while n != 1:
                step += 1
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = n * 3 + 1
            return step
        nums = list(range(lo, hi + 1))
        powers = [power(n) for n in nums]
        sortedIndex = list(range(0, hi - lo + 1))
        sortedIndex = sorted(sortedIndex, key=lambda x: (powers[x], nums[x]))
        return sortedIndex[k - 1] + lo

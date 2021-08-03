class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def at_most_k(k: int) -> int:
            i, j, odds = 0, 0, 0
            res = 0
            while j < n:
                if nums[j] % 2:
                    odds += 1
                while i <= j and odds > k:
                    if nums[i] % 2:
                        odds -= 1
                    i += 1
                j += 1
                res += j - i
            return res

        return at_most_k(k) - at_most_k(k - 1)

from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        nums = sorted(nums)
        for n in nums:
            if c[n] > 0:
                c[n] -= 1
                for i in range(1, k):
                    if c[n + i] == 0:
                        return False
                    c[n + i] -= 1

        return True

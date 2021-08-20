class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        counts = collections.Counter(nums)
        for num in nums:
            if counts[num] > 0:
                for i in range(k):
                    counts[num + i] -= 1
                    if counts[num + i] < 0:
                        return False
        return True

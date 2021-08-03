class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        counts = Counter(nums)
        for num in nums:
            if counts[num] == 0:
                continue
            for i in range(k):
                if counts[num + i] == 0:
                    return False
                counts[num + i] -= 1

        return True

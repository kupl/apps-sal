class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        nums.sort()
        counts = collections.Counter(nums)

        for x in nums:
            if counts[x] == 0:
                continue
            exist_chain = True
            for i in range(k):
                if counts[x + i] == 0:
                    return False
                counts[x + i] -= 1

        return True

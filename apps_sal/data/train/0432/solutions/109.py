from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        cnums = Counter(nums)
        nums.sort()

        for i in nums:
            if cnums[i] == 0:
                continue

            for j in range(i, i + k):
                if cnums[j] == 0:
                    return False
                cnums[j] -= 1

        return True

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        nums.sort()

        index = {}
        for i in nums:
            index[i] = index.get(i, 0) + 1

        for i in index:
            while index[i] > 0:
                for j in range(i, i + k):
                    if index.get(j, 0) > 0:
                        index[j] -= 1
                    else:
                        return False
        return True

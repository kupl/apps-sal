class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        pos = [0] * len(nums)
        neg = [0] * len(nums)
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0
        for i in range(1, len(nums)):
            if nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            elif nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            else:
                pos[i] = 0
                neg[i] = 0
        return max(pos)


'\npos[i] = max length subarray ending at i whose product is positive\nneg[i] = max length subarray ending at i whose product is negative\n\n\npos[i] = (\n    1 + pos[i-1], if nums[i] > 0\n    1 + neg[i-1] elif nums[i] < 0\n    0            else\n)\n\nneg[i] = (\n    1 + neg[i-1], if nums[i] > 0\n    1 + pos[i-1], elif nums[i] < 0\n    0             else\n)\n\nA = [-1,-2,-3,0,1]\np = [0,  2, 2,]\nn = [1,  1, 3]\n\n\n\n[0,1,-2,-3,-4]\n\n[0,1,0,3,2]\n[0,0,2,1,]\n\n\n\n\n'

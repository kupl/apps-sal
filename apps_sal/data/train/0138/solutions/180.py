class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i = 0
        negatives = [-1, -1]
        p = 1
        ans = 0
        for j, n in enumerate(nums):
            if not n:
                p = 1
                i = j + 1
                negatives = [-1, -1]
            else:
                p *= n
                if n < 0:
                    if negatives[0] < 0:
                        negatives[0] = j
                    negatives[1] = j
                if p > 0:
                    ans = max(ans, j - i + 1)
                else:
                    ans = max(ans, negatives[1] - i, j - negatives[0])
        return ans

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        dp = []
        oneIndices = [-1]
        ans = 0
        for i, num in enumerate(A):
            if num == 1:
                oneIndices.append(i)
            if len(oneIndices) >= S + 1:
                if S == 0:
                    ans += (i - oneIndices[-S-1])
                else:
                    ans += (oneIndices[-S] - oneIndices[-S-1])
        return ans

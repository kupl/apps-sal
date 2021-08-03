class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ALen = len(A)
        dictList = [defaultdict(lambda: 1) for _ in range(ALen)]
        ans = 2
        for i, num in enumerate(A):
            for j in range(i - 1, -1, -1):
                delta = A[i] - A[j]
                if delta not in dictList[i]:
                    dictList[i][delta] = 1 + dictList[j][delta]
                    ans = max(ans, dictList[i][delta])
        return ans

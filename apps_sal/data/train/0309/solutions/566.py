class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        DP = [0] * len(A)
        for i in range(len(A)):
            temp = {}
            for j in range(i):
                diff = A[i] - A[j]
                temp[diff] = DP[j].get(diff, 0) + 1
            DP[i] = temp
        return max(max(d.values()) for d in DP if d) + 1

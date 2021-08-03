class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:

        arr = [A[0] + A[j] - j for j in range(1, len(A))]
        print(arr)
        maxdiff = 0
        ans = max(arr)
        for j in range(1, len(arr)):
            maxdiff = max(maxdiff, A[j] - A[0] + j)
            ans = max(ans, arr[j] + maxdiff)
        return ans

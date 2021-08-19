class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        arr = {}
        ans = 0
        for i in range(1, len(A)):
            for j in range(i):
                dif = A[i] - A[j]
                if not arr.get(dif):
                    arr[dif] = [1 for i in range(len(A))]
                arr[dif][i] = arr[dif][j] + 1
                ans = max(ans, arr[dif][i])
        return ans

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cumsums = []
        cumsum = 0
        cumsums.append(cumsum)
        for num in A:
            cumsum += num
            cumsums.append(cumsum)
        n = len(A)
        ans = -float('inf')
        print(cumsums)
        for i in range(0, n - L - M + 1):
            for j in range(i + L, n - M + 1):
                ans = max(ans, cumsums[i + L] - cumsums[i] + cumsums[j + M] - cumsums[j])
        for i in range(0, n - M - L + 1):
            for j in range(i + M, n - L + 1):
                ans = max(ans, cumsums[i + M] - cumsums[i] + cumsums[j + L] - cumsums[j])
        return ans

class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        max_found = 0
        sums = {}
        self.sumsOfL(A, L, sums)
        for i in range(len(A) - M + 1):
            available = self.getAvailableIndices(A, L, M, i)
            current_sum = sum(A[i:i + M])
            for j in available:
                max_found = max(max_found, sums[j] + current_sum)
        return max_found

    def getAvailableIndices(self, A, L, M, i):
        available = []
        for j in range(len(A) - L + 1):
            if j < i - L or j >= i + M:
                available.append(j)
        return available

    def sumsOfL(self, A, L, dictionary):
        left = 0
        right = L
        for i in range(len(A) - L + 1):
            dictionary[left] = sum(A[left:right])
            left += 1
            right += 1

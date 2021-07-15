class Solution:
    def maxWindowSum(self, A, M):
        acc = [A[0]]
        for i in range(1, len(A)):
            acc.append(acc[i-1] + A[i])
        maxSum = sum(A[:M])
        for i in range(M, len(A)):
            maxSum = max(maxSum, acc[i] - acc[i-M])
        return maxSum
            
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        if not A or L+M > n:
            return 0
        left = []
        right = []
        maxSum = 0
        for i in range(n - L + 1):
            maxL = sum(A[i:i+L])
            maxM = 0
            if i >= M:
                left = A[:i]
                maxM = max(maxM,self.maxWindowSum(left, M))
            if n - i - L >= M:
                right = A[i+L:]
                maxM = max(maxM, self.maxWindowSum(right, M))
                
            maxSum = max(maxSum, maxL + maxM)
        return maxSum

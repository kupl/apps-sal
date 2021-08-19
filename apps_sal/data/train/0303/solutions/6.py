class Solution:

    def util(self, i, n, A, K, d):
        if i >= n:
            return 0
        if i not in d:
            count = 0
            ma = A[i]
            temp = -1
            while i + count < n and count <= K - 1:
                if A[i + count] > ma:
                    ma = A[i + count]
                nex = self.util(i + count + 1, n, A, K, d)
                if (count + 1) * ma + nex > temp:
                    temp = (count + 1) * ma + nex
                count += 1
            d[i] = temp
        return d[i]

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        d = {}
        return self.util(0, n, A, K, d)

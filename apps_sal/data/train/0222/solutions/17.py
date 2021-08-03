class Solution:
    def lenLongestFibSubseq1(self, A: List[int]) -> int:
        '''
        time complexity: O(N^2logM)
        '''
        s = set(A)
        n = len(A)
        res = 2

        for i in range(n):
            for j in range(i + 1, n):
                a = A[i]
                b = A[j]
                length = 2
                while a + b in s:
                    a, b, length = b, a + b, length + 1
                res = max(res, length)
        return res if res > 2 else 0

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        '''
        dp[i][j] represents the length of fibo sequence ends up with (A[i], A[j])
        '''
        map = collections.defaultdict(int)
        for i, v in enumerate(A):
            map[v] = i
        n = len(A)
        res = 2
        dp = [[2 for _ in range(n + 1)] for _ in range(n + 1)]
        for j in range(n):
            for i in range(j):
                diff = A[j] - A[i]
                if diff in map and map[diff] < i:
                    k = map[diff]
                    dp[i][j] = 1 + dp[k][i]
                    res = max(dp[i][j], res)
        return res if res > 2 else 0

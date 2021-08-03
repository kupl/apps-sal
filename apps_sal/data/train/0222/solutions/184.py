class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        record = {}
        for i, a in enumerate(A):
            record[a] = i

        adj = {}
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                if (A[i] + A[j]) in record:
                    adj[(i, j)] = (j, record[A[i] + A[j]])

        mem = {}

        def helper(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            else:
                if (i, j) in adj:
                    res = 1 + helper(adj[(i, j)][0], adj[(i, j)][1])
                    mem[(i, j)] = res
                    return res
                else:
                    mem[(i, j)] = 2
                    return 2
        res = 0
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                res = max(res, helper(i, j))
        if res >= 3:
            return res
        else:
            return 0

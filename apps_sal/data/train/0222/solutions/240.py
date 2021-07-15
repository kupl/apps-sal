class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        A_map = {x: i for i, x in enumerate(A)}
        
        M = [[2] * len(A) for _ in range(len(A))]
        
        # M[j][k] = longest fib subsequence ending with elements (A[j], A[k])
        #           = 1 + max(M[i][j]) over i, if A[i] + A[j] = A[k]
        
        best = 0
        for k in range(len(A)):
            for j in range(k):
                i = A_map.get(A[k] - A[j], None)
                if i is not None and i < j:
                    M[j][k] = M[i][j] + 1
                    best = max(best, M[j][k])
        # for row in M:
        #     print(row)
        
        return best if best >= 3 else 0

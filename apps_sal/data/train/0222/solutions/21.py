class Solution:
    # brute-force time O(n^2logm), m是A的最大值,代码在下面
    # 试试机械dp, time O(n^2), space O(n^2)
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        M = [[-1 for i in range(n)] for i in range(n)]
        mapping = {v:i for i, v in enumerate(A)}
        ret = 0
        
        def dp(prev_, next_):
            if next_ == n-1:
                return 1
            
            if M[prev_][next_] != -1:
                return M[prev_][next_]
            
            M[prev_][next_] = 1
            if A[prev_]+A[next_] in mapping:
                M[prev_][next_] += dp(next_, mapping[A[prev_]+A[next_]])
            return M[prev_][next_]
        
        for i in range(n):
            for j in range(i+1, n):
                if A[i]+A[j] in mapping:
                    ret = max(ret, 2+dp(j, mapping[A[i]+A[j]]))
        
        return ret if ret > 2 else 0
#     def lenLongestFibSubseq(self, A: List[int]) -> int:
#         ret = 0
#         n = len(A)
#         mapping = {v:i for i, v in enumerate(A)}
        
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 prev_, next_ = A[j], A[i]+A[j]
#                 length = 2
#                 while next_ in mapping:
#                     length += 1
#                     prev_, next_ = next_, prev_+next_
                
#                 if length > 2:
#                     ret = max(ret, length)
        
#         return ret


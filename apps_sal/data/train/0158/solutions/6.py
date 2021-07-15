# class Solution:
#     def kSimilarity(self, A: str, B: str) -> int:
#         n = len(A)
#         A, B = list(A), list(B)
#         mp = defaultdict(list)
#         for i, ch in enumerate(A):
#             mp[ch].append(i)
#         def dfs(idx):
#             if idx == n:
#                 return 0
#             if A[idx] == B[idx]:
#                 return dfs(idx+1)
#             res = float('inf')
#             for nxt in range(idx+1,n):
#                 if A[nxt] != B[idx]:
#                     continue
#                 A[idx], A[nxt] = A[nxt], A[idx]
#                 res = min(res, dfs(idx+1)+1)
#                 A[idx], A[nxt] = A[nxt], A[idx]
#             return res
#         return dfs(0)

from functools import lru_cache
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        n = len(A)
        # mp = defaultdict(list)
        # for i, ch in enumerate(A):
        #     mp[ch].append(i)
        @lru_cache(None)
        def dfs(s):
            if s == B:
                return 0
            idx = 0
            while s[idx] == B[idx]:
                idx += 1
            res = float('inf')
            for nxt in range(idx+1,n):
                if s[nxt] != B[idx]:
                # if s[nxt] != B[idx] or s[nxt] == B[nxt]:
                    continue
                res = min(res, dfs(s[:idx]+s[nxt]+s[idx+1:nxt]+s[idx]+s[nxt+1:])+1)
            return res
        return dfs(A)

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # self.res = float('-inf')
        self.A, self.B = A, B
        self.seen = {}
        return self.dfs(0, 0)
                
    def dfs(self, a, b):
            m, n = len(self.A), len(self.B)
            if a >= m or b >= n:
                return 0
            if (a, b) in self.seen:
                return self.seen[(a, b)]
            
            res = float('-inf')
            cur_b = b
            if self.A[a] == self.B[b]:
                res = max(res, self.dfs(a + 1, b + 1) + 1)
#             while cur_b < n:
#                 if self.A[a] == self.B[cur_b]:
#                     res = max(res, self.dfs(a + 1, cur_b + 1) + 1)
#                     break
#                 cur_b += 1
                
#             cur_a = a
#             while cur_a < m:
#                 # print(cur_a, b)
#                 if self.A[cur_a] == self.B[b]:
#                     res = max(res, self.dfs(cur_a + 1, b + 1) + 1)
#                     break
#                 cur_a += 1
            res = max(res, self.dfs(a + 1, b))
            res = max(res, self.dfs(a, b + 1))
            
            self.seen[(a, b)] = res
            return res

class Solution:
    def maxJumps(self, A: List[int], d: int) -> int:
        N = len(A)
        jumpable = collections.defaultdict(list)
        
        def find_jumpable_indices(iter):
            stack = []
            for i in iter:
                while stack and A[stack[-1]] < A[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        jumpable[i].append(j)
                stack.append(i)

        find_jumpable_indices(list(range(N)))
        find_jumpable_indices(reversed(list(range(N))))
        
        dp = [-1] * N
        def dfs(idx):
            if dp[idx] > -1:
                return dp[idx]
            res = 1
            for j in jumpable[idx]:
                res = max(res, 1 + dfs(j))
            
            dp[idx] = res
            return res
        
        return max(list(map(dfs, list(range(N)))))


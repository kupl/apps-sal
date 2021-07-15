class Solution:
    def knightDialer(self, n: int) -> int:
#         board = [[str(j) for j in (1 + 3*i, 3*i + 2, 3*i + 3)] for i in range(3)]
#         board.append(['*', '0', '#'])
#         direct = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
#         dp = {}
#         def dfs(i, j, step):
           
#             if i < 0 or i > 3 or j < 0 or j > 2: return 0
#             if board[i][j] in '*#': return 0
#             if step == 1: return 1
#             key = (board[i][j], step)
#             if key in dp: return dp[key]
#             dest = set([(i + dr, j + dc) for  dr, dc in direct])
#             dp[key] = sum([dfs(r, c, step - 1) for r, c in dest])
#             return dp[key]
        
#         res = 0
#         for i in range(10):
#             res += dfs(str(i), n)
#         return res%(10**9 + 7)
        dp  = {}
        def nextStep(k):
            if k == 1: return [6, 8]
            if k == 2: return [7, 9]
            if k == 3: return [4, 8]
            if k == 4: return [9, 3, 0]
            if k == 6: return [7,1,0]
            if k == 7: return [6,2]
            if k == 8: return [1,3]
            if k == 9: return [4,2]
            if k == 0: return [4, 6]
            
        def dfs(k, step):
            if k == 5 and step > 1: return 0
            if step == 1: return 1
            key = (k, step)
            if key in dp: return dp[key]
            dp[key] = sum([dfs(e, step - 1) for e in nextStep(k)])  
            return dp[key]
        res = 0
        for i in range(10):
            # if i ==5:continue
            res += dfs(i, n)
        return res%(10**9 + 7)
            


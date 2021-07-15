class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0
        for i in range(n-2):
            for j in range(i + 1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        total += 1
                    elif rating[i] > rating[j] and rating[j] > rating[k]:
                        total += 1
        
        return total
#         n = len(rating)
#         grid = [[0 for i in range(n)] for i in range(n)]
        
#         for win in range(3, n+1):
#             for start in range(n - win + 1):
#                 end = start + win - 1
#                 count = 0
#                 for num in rating[start+1: start + win-1]:
                    
#                     if rating[start] < num and rating[end] > num:
#                         count += 1
#                         print(rating[start], num, rating[end])
#                 print(count)
#                 grid[start][end] = grid[start + 1][end] + grid[start][end-1] + count
        
#         ascend = grid[0][n-1]
        
#         for i in range(n):
#             for j in range(n):
#                 grid[i][j] = 0
                
                
#         for win in range(3, n+1):
#             for start in range(n - win + 1):
#                 end = start + win - 1
#                 count = 0
#                 for num in rating[start+1: start + win-1]:
                    
#                     if rating[start] > num and rating[end] < num:
#                         count += 1
#                         print(rating[start], num, rating[end])
                
#                 grid[start][end] = grid[start + 1][end] + grid[start][end-1] + count
        
#         descend = grid[0][n-1]
        
#         print(ascend)
#         print(descend)
        
#         return ascend + descend


class Solution:
    def knightDialer(self, n: int) -> int:
        move = {1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}
        
        curr_dial = [1] * 10
        for _ in range(n-1):
            next_dial = [0] * 10
            for key in range(10):
                for neighbor in move[key]:
                    next_dial[neighbor] = (next_dial[neighbor] + curr_dial[key]) % (10 ** 9 +7)
                
            curr_dial = next_dial
            
        return sum(curr_dial) % (10 ** 9 +7)
    
#         case = set()
        
#         def dfs(curr = \"\", k = 0):
#             if k == n:
#                 case.add(curr)
#                 return
#             if k == 0:
#                 for i in range(10):
#                     dfs(curr + str(i), k+1)
#             else:
#                 for i in move[int(curr[-1])]:
#                     dfs(curr + str(i), k+1)
        
#         dfs()    
            
#         return len(case) % (10 ** 9 +7)


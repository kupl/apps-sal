class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 10**9 + 7
        
        dp = [1] * 10 
        
        while n > 1:
            new_table = [0] * 10
            for digit in range(10):
                for neighbor in self.getNeighbor(digit):
                    new_table[neighbor] += dp[digit]
            dp = new_table
            n -= 1
            
        return sum(dp) % (modulo)
            
#     def getWays(self, curr, steps):
#         if steps == 0:
#             return 1 
#         if (curr, steps) in self.cache:
#             return self.cache[(curr,steps)]
#         temp = 0
#         for digit in self.getNeighbor(curr):
#             temp += self.getWays(digit,steps-1)
          
#         self.cache[(curr,steps)] = temp
        
#         return temp
            
    
    def getNeighbor(self, digit):
        neighbors = {
            1: (6,8),
            2: (7,9),
            3: (4,8),
            4: (0,3,9),
            5: (),
            6: (0,1,7),
            7: (2,6),
            8: (1,3),
            9: (2,4),
            0: (4,6)
        }
        
        return neighbors[digit]
    


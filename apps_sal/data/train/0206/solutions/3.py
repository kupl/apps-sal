class Solution:
     def PredictTheWinner(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         
         """
         memo = [ [0 for _ in range(len(nums))] for _ in range(len(nums))]
         self.count=0
         
         def winner( left , right , player):
             self.count +=1
             #print(self.count)
             if left == right:
                 
                 return player * nums[left]
            
             # p1 selct max from each end
             # remove the selected
             # p2 selects max from each end
             # do above seps until no mor num
             # 1 5 2
             #print( left, right)
             
             if memo[left][right] != 0 :
                 print((nums[left:right+1]))
                 return memo[left][right]
            
             #self.count +=1
             a = player * nums[left] + winner( left+1 , right, -player )
             
             #self.count +=1
             b = player * nums[right] + winner( left , right -1 , -player)
             
             
             
             if player == 1:
                 res = max(a,b)
             else:
                 res = min(a,b)
                 
             memo[left][right] = res
             
             return res
             
         self.count=0    
         return winner( 0, len(nums) -1 , 1) >=0 
         
             
                 
         


class Solution:
     def canPartitionKSubsets(self, nums, k):
         quotient = sum(nums)/k
         if quotient % 1 != 0:
             return False
         
         for num in nums:
             if num > quotient:
                 return False
             if num == quotient:
                 nums.remove(quotient)
                 k -= 1
         nums.sort(reverse=True)
         self.nums = nums
         self.quotient = quotient
         print(self.nums)
         
         answer = self.dfs([0]*len(nums), 0, k)
         return answer
 #        print(answer)
     
     def dfs(self, visit, accu, k):
         if k == 1:
 #            print(visit)
             return True
         
         for i in range(len(self.nums)):
             if not visit[i]:
                 #print(visit)
                 if self.nums[i] + accu < self.quotient:
                     visit[i] = 1
                     if self.dfs(visit, self.nums[i] + accu, k):
                         return True
                     visit[i] = 0
                 if self.nums[i] + accu == self.quotient:
                     visit[i] = 1
                     accu = self.nums[i] + accu
                     return self.dfs(visit, 0, k-1)
         return False

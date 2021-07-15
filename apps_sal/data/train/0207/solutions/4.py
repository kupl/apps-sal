class Solution:
     def largestNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: str
         """
         # case 1  34 vs 34
         #case2: 3 vs 34  ;    34 vs 3;        30 vs 3;  3 vs 30
 
         # this works:
         # compare the element by ourselves according to the rule of largest number first    
         if nums is None or len(nums) == 0:
             return ''
 
         for i in range(len(nums)-1, -1, -1):
             for j in range(len(nums)-1, len(nums)-i-1, -1):
                 #compare element 1, 2
                 e1 = str(nums[j-1])
                 e2 = str(nums[j])
                 #print ("e1, e2: ", e1, e2, nums)
                 if e1+e2 < e2+e1:
                     #swap 
                     t = nums[j]
                     nums[j] = nums[j-1]
                     nums[j-1] = t
 
         ans = ''
         for n in nums:
             if n == 0 and ans == '':
                 continue
             ans += str(n)
         #print ("nums: ", nums)
         return '0' if len(ans) == 0 else ans 


class Solution:
     def largestNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: str
         """
         
         ## edge case: 981 3,31 331 313
         
         
         strs = [str(num) for num in nums]
         
         def bigger(str1, str2):
             if int(str1+str2) >= int(str2+str1):
                 return str1
             else:
                 return str2
         
         answer = ""
         current = strs
         while current:
             maximum = current[0]
             for i in range(len(current)):
                 maximum = bigger(maximum, current[i])
                 
             answer += maximum
             current.remove(maximum)
         
         if answer[0] == "0":
             return "0"
         return answer

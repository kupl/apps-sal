class Solution:
     def plusOne(self, digits):
         """
         :type digits: List[int]
         :rtype: List[int]
         """
         flag = 1
         i = len(digits)-1
         while i >=0:
             if digits[i]+flag <10:
                 digits[i] = digits[i]+flag
                 flag = 0
             else:
                 digits[i] = (digits[i]+flag)%10
             i-=1
         if flag == 1:
             digits.insert(0,1)
         return digits

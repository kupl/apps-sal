class Solution:
     def plusOne(self, digits):
         """
         :type digits: List[int]
         :rtype: List[int]
         """
         if not digits:
             return [1]
         carry = 1
         for i in reversed(range(len(digits))):
             if carry == 0:
                 return digits
             carry, digits[i] = (digits[i] + carry) // 10, (digits[i]+carry) % 10
         if carry:
             return [1] + digits
         return digits

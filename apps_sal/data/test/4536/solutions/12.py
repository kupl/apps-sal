class Solution:
     def plusOne(self, digits):
         """
         :type digits: List[int]
         :rtype: List[int]
         """
         num = 0
         for i in range(len(digits)):
             num += 10**i * digits[len(digits)-i-1]
         return(list(map(int, list(str(num+1)))))


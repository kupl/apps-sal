class Solution:
     V1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
     V2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
     V3 = ["Thousand", "Million", "Billion"]
 
     def numberToWords(self, num):
         """
         :type num: int
         :rtype: str
         """
         if num == 0:
             return "Zero"
         
         answer = self.convert_hundred(num % 1000)
         for i in range(3):
             num //= 1000
             
             if num % 1000 > 0:
                 following = " " + answer if answer else ""
                 answer = self.convert_hundred(num % 1000) + " " + self.V3[i] + following
 
         return answer
 
     def convert_hundred(self, num):
         answer = ""
         
         a = num // 100
         b = num % 100
         c = num % 10
         
         if b < 20:
             answer = self.V1[b]
         else:
             following = " " + self.V1[c] if c > 0 else ""
             answer = self.V2[b // 10] + following
         
         if a > 0:
             following = " " + answer if answer else ""
             answer = self.V1[a] + " Hundred" + following
         
         return answer


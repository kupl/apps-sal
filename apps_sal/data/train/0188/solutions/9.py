class Solution:
 
     quantity_unit = ['', 'Thousand', 'Million', 'Billion']
     digit_to_str = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine']
 
     ten_to_str = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                   17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                   60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: ''}
 
     def read_three_digits(self, unit, ten, hundred, index):
 
         if ten == 1:
             str_of_num = ' ' + Solution.ten_to_str[ten * 10 + unit]
         else:
             str_of_num = (' ' + Solution.ten_to_str[ten * 10] + Solution.digit_to_str[unit]) if ten > 1 else Solution.digit_to_str[unit]
 
         str_of_num = (Solution.digit_to_str[hundred] + ' Hundred' if hundred > 0 else "") + str_of_num
         # print(str_of_num + str(index))
         return str_of_num[1:] + ' ' + Solution.quantity_unit[index] if str_of_num else str_of_num[1:]
 
     def numberToWords(self, num):
         """
         :type num: int
         :rtype: str
         """
         if num == 0:
             return 'Zero'
 
         str_of_num = ""
         index = 0
         while num > 0:
             part = num % 1000
             unit = part % 10
             ten = (part % 100) // 10
             hundred = part // 100
             str_of_num = self.read_three_digits(unit, ten, hundred, index) + ' ' + str_of_num.strip()
             num //= 1000
             index += 1
         return str_of_num.strip()

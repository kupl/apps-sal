class Solution:
     def numberToWords(self, num):
         """
         :type num: int
         :rtype: str
         """
         num_lyst = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
         tens_lyst = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
         under20_lyst = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
         large_scale = ['', 'Thousand', 'Million', 'Billion']
         
         def convert(num):
             out_str = ''
             hundred = num // 100
             ten_digit = num % 100
             if hundred:
                 out_str += num_lyst[hundred] + ' ' + 'Hundred '
             if ten_digit:
                 if ten_digit < 10:
                     out_str += num_lyst[ten_digit]
                 elif ten_digit < 20:
                     out_str += under20_lyst[ten_digit % 10]
                 else:
                     out_str += tens_lyst[ten_digit // 10] + ' ' + num_lyst[ten_digit % 10]
                     
             return out_str.strip()
         
         if not num:
             return 'Zero'
         
         
         res = num // 1000    # 商
         last3 = num % 1000     # 余数，后三位
         ans = ''
 
         while res or last3:
             if last3:
                 ans = convert(last3) + ' ' + large_scale.pop(0) + ' '+ ans
             else:
                 large_scale.pop(0)
             
             last3 = res % 1000
             res = res //1000
             
         return ans.strip()
                 
             
                 
                 
             
             


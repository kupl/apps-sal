class Solution:
     def removeKdigits(self, num, k):
         """
         :type num: str
         :type k: int
         :rtype: str
         """
         while True:
             if k == 0:
                 return num if num != "" else "0"
             if num == "":
                 return "0"
             index = 0
             num_len = len(num)
             while True:
                 if index == num_len - 1:
                     num = num[:-1]
                     k -= 1
                     break
                 if num[index] > num[index + 1]:
                     new_num = num[:index] + num[index+1:]
                     num = new_num.lstrip("0")
                     k -= 1
                     break
                 index += 1

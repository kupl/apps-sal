class Solution:
     def largestNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: str
         """
         def cmp_to_key(mycmp):
             'Convert a cmp= function into a key= function'
             class K:
                 def __init__(self, obj, *args):
                     self.obj = obj
                 def __lt__(self, other):
                     return mycmp(self.obj, other.obj) < 0
                 def __gt__(self, other):
                     return mycmp(self.obj, other.obj) > 0
                 def __eq__(self, other):
                     return mycmp(self.obj, other.obj) == 0
                 def __le__(self, other):
                     return mycmp(self.obj, other.obj) <= 0
                 def __ge__(self, other):
                     return mycmp(self.obj, other.obj) >= 0
                 def __ne__(self, other):
                     return mycmp(self.obj, other.obj) != 0
             return K
         
         def compare(n1, n2):
             #print(n1, n2, ":")
             l1 = len(n1)
             l2 = len(n2)
             i = 0
             if l1 != l2:
                 tmp = n1 
                 n1 = n1 + n2
                 n2 = n2 + tmp
                 l1 = l1 + l2
             #print(n1, n2)
             while i < max(l1, l2):
                 #print(i, n1[i], n2[i])
                 if n1[i] < n2[i]:
                     #print(n1, "<", n2)
                     return -1
                 elif n1[i] > n2[i]:
                     #print(n1, ">", n2)
                     return 1
                 i += 1
             #print(n1, "=", n2)
             return 0
             
         
         def convert(num):
             if num == 0:
                 return [0]
             res = []
             while num:
                 res.append(num % 10)
                 num //= 10
             res.reverse()
             return res
         
         nums = list(map(convert, nums))
         nums.sort(key=cmp_to_key(compare), reverse=True)
         print(nums)
         res = [str(c) for num in nums for c in num]
         
         res =  "".join(res).lstrip('0')
         if not res:
             res = '0'
         return res

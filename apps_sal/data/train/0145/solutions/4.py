class Solution(object):
     def judgePoint24(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         
         def cal(operands, operaters):
             for opt in operaters:
                 op2, op1 = operands.pop(-1), operands.pop(-1)
                 if opt=='+':
                     ret = op1+op2
                 elif opt=='-':
                     ret = op1-op2
                 elif opt=='*':
                     ret = op1*op2
                 elif opt=='/' and op2!=0:
                     ret = op1/op2
                 else:
                     return float('-inf')
                 operands.append(ret)
             
             return operands[0] if abs(operands[0]-24)>0.0000001 else 24
         
         def comb(arr):
             if len(arr)==1:
                 return [arr]
             ret = []
             for i in range(len(arr)):
                 if i-1>=0 and arr[i]==arr[i-1]:
                     continue
                 for remain in comb(arr[:i]+arr[i+1:]):
                     ret.append([arr[i]]+remain)
             return ret
         
         def genopt(n):
             if n==0:
                 return ['']
             ret = []
             for i in '+-*/':
                 for res in genopt(n-1):
                     ret.append(i+res)
             return ret
         
         nums.sort()
         ops = comb(nums)
         opts = genopt(3)
         for op in ops:
             for opt in opts:
                 if cal(op[:], opt)==24:
                     return True
                 
         def base(a, b):
             return set([a+b,a-b,b-a,a*b]+([a/b] if b!=0 else[])+([b/a] if a!=0 else[]))
             
         for i in range(4):
             for j in range(i+1, 4):
                 a, b = nums[i], nums[j]
                 remain = nums[:i]+nums[i+1:j]+nums[j+1:4]
                 for x in base(a, b):
                     for y in base(remain[0], remain[1]):
                         if 24 in base(x, y):
                             return True
                 
         
         return False

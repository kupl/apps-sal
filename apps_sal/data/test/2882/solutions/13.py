class Solution:
     def generateParenthesis(self, n):
         """
         :type n: int
         :rtype: List[str]
         """
         
         def balance(str):
             lst = list(str)
             bal = 0
             for char in lst:
                 if char == "(":
                     bal += 1
                 else:
                     bal -= 1
             return bal
         
         def left(str):
             lst = list(str)
             sum = 0
             for char in lst:
                 if char == "(":
                     sum += 1
             return n - sum
         
         def right(str):
             lst = list(str)
             sum = 0
             for char in lst:
                 if char == ")":
                     sum += 1
             return n - sum
         
 
         prev = ["("]
         length = 1
         
         while length < 2*n:
             current = [] 
                 
             for item in prev:
                 if left(item) != 0:
                     current.append(item+"(")
                     
                 if right(item) != 0 and balance(item) > 0:
                     current.append(item+")")
             length += 1
             prev = current
         
         return prev

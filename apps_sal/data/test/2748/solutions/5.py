from functools import reduce
 
 class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         
         d = {}
         d["1"] = ""
         d["2"] = "abc"
         d["3"] = "def"
         d["4"] = "ghi"
         d["5"] = "jkl"
         d["6"] = "mno"
         d["7"] = "pqrs"
         d["8"] = "tuv"
         d["9"] = "wxyz"
         d["0"] = " "
         
         digs = list(map(lambda x: list(d[x]), digits))
         
         return reduce(alg_mul, digs, [])
                 
 
 def alg_mul(xs, ys):
     if xs == []:
         return ys
     
     ws = []
     for x in xs:
         for y in ys:
             ws.append(x + y)
     
     return ws

class Solution:
     def fractionToDecimal(self, numerator, denominator):
         """
         :type numerator: int
         :type denominator: int
         :rtype: str
         """
         sign=0
         if numerator*denominator<0:
             sign =-1
         numerator,denominator = abs(numerator),abs(denominator)
         n = numerator
         s =''
         if n >denominator:
             s +=str(n//denominator)
             n %=denominator
         else:
             s ='0'
         if sign==-1:
             s = '-'+s
         if n == 0:
             return s
         s +='.'
         t =[n]
         x = n
         s1=''
         while 1:
             x *=10
             s1 +=str(x//denominator)
             x %=denominator
             if x in t or  x==0:
                 break
             else:
                 t.append(x)
         if x in t:
             s1=s1[:t.index(x)]+'('+s1[t.index(x):]+')'
 
             
         return s+s1


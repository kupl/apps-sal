class Solution:
     def findIntegers(self, num):
         """
         :type num: int
         :rtype: int
         """
         def func(num):
             if num<3:
                 return num+1
             t,k=num,-1
             while t:
                 t>>=1
                 k+=1
             if (num>>(k-1))^3==0:
                 return a[k-1]+a[k]
             return a[k]+func(num-(1<<k))
         
         t,k,a=num,-1,[1,2]
         while t:
             t>>=1
             k+=1
         for i in range(1,k):
             a.append(a[-1]+a[-2])
         return func(num)

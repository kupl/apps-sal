class Solution(object):
     def findKthNumber(self, n, k):
         """
         :type n: int
         :type k: int
         :rtype: int
         """
         s,nn=0,str(n)
         while nn:
             if not k: return s
             c,m=0,10**(len(nn)-1)
             mm,p,t=(m-1)//9,int(nn)//m,0
             for i in range(1 if not s else 0,p):
                 cc=c+m+mm
                 if cc>=k:
                     s=10*s+i
                     k-=c+1
                     nn='9'*(len(nn)-1)
                     t=1
                     break
                 c=cc
             if not t:
                 cc=c+int(nn)-(m*p)+1+mm
                 if cc>=k:
                     s=10*s+p
                     k-=c+1
                     nn=nn[1:]
                 else:
                     c=cc
                     for i in range(p+1,10):
                         cc=c+mm
                         if cc>=k:
                             s=10*s+i
                             k-=c+1
                             nn='9'*(len(nn)-2)
                             break
                         c=cc
         return s

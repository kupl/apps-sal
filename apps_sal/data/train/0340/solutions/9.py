class Solution:
     def simplifyPath(self, path):
         """
         :type path: str
         :rtype: str
         """
         n=len(path)
         if(n==0): return path
 
         v=[]
         i=0
         while(i<n):
             while(i<n and path[i]=='/' ):i=i+1
             if (i == n): break
             
             left=i
             while(i<n and path[i]!='/'):i=i+1
             right=i-1
             
             s=path[left:right+1]
             
             if s=="..":
                 if (len(v)!=0):
                     v.pop() 
             elif s!= ".":
                 v.append(s)
 
         if(len(v)==0):
             return "/"
         
         ret=''
         for i in range(len(v)):
             ret=ret+'/'+v[i]
 
         return ret

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        if lo==hi==k==1:return 1
        dic={}
        def fun(n,count):
            if n==1:return count
            count+=1
            if n%2==0:n//=2
            else:n=n*3+1
            if n in dic:return count+dic[n]
            return fun(n,count)
        ans=[] 
        for i in range(lo,hi+1):
            dic[i]=fun(i,0)
        return sorted(list(dic.items()),key=lambda x :x[1])[k-1][0]
        


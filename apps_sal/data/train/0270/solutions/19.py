class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s=''
        l=['a','b','c']
        self.count=0
        self.res=''
        def alls(n,s,k):
            for i in l:
                if(len(s)!=0):
                    if(s[-1]==i):
                        continue
                if(n==0):
                    self.count+=1
                    if(self.count==k):
                        self.res=s
                        return self.res
                    break
                n-=1
                s+=i
                alls(n,s,k)
                n+=1
                s=s[:-1]
            return self.res
        return alls(n,s,k)

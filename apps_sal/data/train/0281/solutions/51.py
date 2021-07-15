class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if(s==t):
            return True
        if(len(s)!=len(t)):
            return False
        has={}
        for i in range(1,27):
            num=26+i
            if(i<=k):
                has[i]=1
                x=(k-i)//26
                has[i]+=x
        n=len(s)
        print(has)
       
        count=0
        for i in range(n):
            if(s[i]==t[i]):
                count+=1
                continue
            diff=(ord(t[i])-ord(s[i]))%26

            if(diff in has):
                count+=1
                has[diff]-=1
                if(has[diff]==0):
                    del has[diff]
            else:
                return False
        # print(has2)
        if(count==n):
            return True
        return False
                
            
            
            
            


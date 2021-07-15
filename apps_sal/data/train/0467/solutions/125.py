class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0
        for val in nums:
            P=self.check(val)
            if P:
                ans+=sum(P)
        return ans
    
    
    
    def check(self,n):
        L=[n]
        count=1
        if n!=1:
            L.append(1)
            count+=1
        
        for i in range(2,int(n**0.5)+1):
            
            if n%i==0:
                L.append(i)
                count+=1
                if n/i!=float(i):
                    L.append(n//i)
                    count+=1
                if count>4:return None
        if count!=4:
            return None
        return L

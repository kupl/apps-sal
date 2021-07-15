class Solution:

    
    def minDays(self, n: int) -> int:
        cur={n}
        res=0
        while cur:
            temp=set()
            for x in cur:
                if x==0: return res
                temp.add(x-1)
                if x%2==0: temp.add(x//2)
                if x%3==0: temp.add(x//3)
            res+=1
            cur=temp
        return res
                
        


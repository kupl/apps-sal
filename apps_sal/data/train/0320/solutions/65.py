class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = 0
        res = 0
        double = 0
        
        for i in nums:
            count = 0
            while i:
                if i%2 == 1:
                    i-=1
                    res+=1
                else:
                    i//=2
                    count+=1
            double= max(double, count)
        
        return res+double

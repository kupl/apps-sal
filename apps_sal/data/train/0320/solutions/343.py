class Solution:
    def minOperations(self, nums: List[int]) -> int:
        plus = 0
        double = 0
        for x in nums:
            if(x!=0):
                plus+=1
            counter =0
            while(x/2>=1):
                if(x%2!=0 and x!=1):
                    plus+=1
                    x-=1
                x/=2
                counter+=1
            double = max(double,counter)
        return plus+double

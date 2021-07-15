class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        
        def findFactors(num):
            if num==0:
                return 0
            res = set()
            for i in range(int(num**0.5)+1):                
                if num%(i+1)==0:
                    res.add(i+1)
                    res.add(num//(i+1))
                    
            return [len(res),sum(res)]
        output = 0
        for num in nums:
            c,sm = findFactors(num)
            # print(c,sm)
            if c==4:
                output+=sm
        return output

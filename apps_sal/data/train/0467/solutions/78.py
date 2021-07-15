class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def helper(n):
            if int(math.sqrt(n)) * int(math.sqrt(n)) == n:
                return 0
            summary = 1 + n
            count = 2
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    summary += (n//i + i)
                    count += 2
                    if count > 4:
                        break
            
            if count == 4: 
                return summary  
            else: 
                return 0
        res = 0
        
        for n in nums:
            res += helper(n)
                
        return res

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            curr = 0
            div_sum = 0
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    curr += 2
                    
                    if i == num // i:
                        div_sum -= i
                        curr -= 1
                        
                    div_sum += i
                    div_sum += (num // i)
        
            if curr == 4:
                res += div_sum
        
        return res


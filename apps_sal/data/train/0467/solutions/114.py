

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        
        div_sum = 0
        
        for num in nums:
            divs = set()
            for i in range(1, floor(sqrt(num))+1):
                if num % i == 0:
                    divs.add(num//i)
                    divs.add(i)
                if len(divs) > 4:
                    break
            if len(divs) == 4:
                div_sum += sum(divs)
        return div_sum

       


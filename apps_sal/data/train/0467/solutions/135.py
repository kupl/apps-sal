class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            div = set()
            for j in range(1,int(sqrt(num)) + 1):
                if not num%j:
                    div.add(j)
                    div.add(num//j)
                if len(div) > 4:
                    break
            if len(div) == 4:
                res += sum(div)
        return res
        


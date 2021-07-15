class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def NOD(x):
            divisor = set([1,x])
            for i in range(2,int(x**.5) + 1):
                if not x%i:
                    divisor.add(i)
                    divisor.add(x//i)
            return divisor
        ans = []
        for num in nums:
            divisor = NOD(num)
            if len(divisor) == 4:
                ans.append(divisor)
        return sum([sum(i) for i in ans])
        


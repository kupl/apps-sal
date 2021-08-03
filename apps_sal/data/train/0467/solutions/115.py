class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def findFactors(num):
            res = set()
            for i in range(int(num**0.5) + 1):
                if num % (i + 1) == 0:
                    res.add(i + 1)
                    res.add(num // (i + 1))
                if len(res) > 4:
                    break
            if len(res) == 4:
                return sum(res)
            else:
                return 0

        output = 0
        for num in nums:
            temp = findFactors(num)
            output += temp
        return output

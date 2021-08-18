class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def getDivs(num):
            result = []
            for div in range(1, int(num**(1 / 2)) + 1):
                if num % div == 0:
                    result.append(div)
                    result.append(num // div)
                if len(result) > 4:
                    print(num, result)
                    return 0

            if (int(num**(1 / 2))) * (int(num**(1 / 2))) == num:
                result.pop()

            if len(result) == 4:
                return sum(result)
            else:
                return 0

        total = 0
        for num in nums:
            total += getDivs(num)

        return total

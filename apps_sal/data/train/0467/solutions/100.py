class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            sqrt = int(math.sqrt(num))
            if sqrt * sqrt == num:
                continue
            divSum = 0
            count = 0
            for i in range(1, sqrt + 1):
                if num % i == 0:
                    divSum += i + num // i
                    count += 1
                    if count > 2:
                        break
            if count == 2:
                ret += divSum
        return ret

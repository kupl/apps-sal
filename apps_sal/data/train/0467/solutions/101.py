class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def getDivisors(k):
            (count, second) = (0, 0)
            for i in range(2, int(sqrt(k)) + 1):
                if k % i == 0:
                    count += 1
                    if count > 1 or i * i == k:
                        return [0]
                    second = k // i
            if count == 1:
                return [1, second, k // second, k]
            else:
                return [0]
        total = 0
        for num in nums:
            total += sum(getDivisors(num))
        return total

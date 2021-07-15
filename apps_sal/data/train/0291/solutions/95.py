class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sumEven = 0
        sumOdd = 0
        cumSum = 0
        
        result = 0
        for num in arr:
            cumSum += num
            if cumSum % 2 == 1:
                result += 1 + sumEven
                sumOdd += 1
            else:
                result += sumOdd
                sumEven += 1
        
        return result % (10**9+7)


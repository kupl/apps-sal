class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        target = 2 * N 
        results = 0
        for k in range(1, int(sqrt(target))+1): 
            if target % k == 0:
                num = (target / k) - k - 1 
                if num >= 0 and num % 2 == 0:
                    results += 1
        return results

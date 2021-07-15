class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        def verify_even(k):
            return N % k != 0 and (2 * N) % k == 0
        
        def verify_odd(k):
            return N % k == 0
        
        count = 0
        
        # Find all odd factors
        for i in range(1, int(math.sqrt(2 * N)) + 1, 1):
            if i % 2 == 0 and verify_even(i):
                count += 1
            elif i % 2 == 1 and verify_odd(i):
                count += 1
                
                
        return count

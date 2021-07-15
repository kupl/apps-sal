class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        def triangle(n):
            return int(n * (n+1) / 2)

        def consecutive_sums(k):
            counter = 0
            n = 1
            while triangle(n) <= k:
                if (k - triangle(n)) % n == 0:
                    X = int((k - triangle(n)) // n)
                    if n != 1:
                        counter += 1
                n += 1
            return counter + 1
        
        return consecutive_sums(N)


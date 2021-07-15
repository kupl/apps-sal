class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        for i in range(1, int(math.sqrt(N))+1):
            if N%i == 0:
                if i%2:
                    count += 1
                if (N/i)%2 != 0 and N/i != i:
                    count += 1
        return count


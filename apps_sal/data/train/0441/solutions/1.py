import math


class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        num = N
        if num == 1:
            return 1
        counter = 1
        for i in range(2, math.floor(math.sqrt(num) + 1)):
            if num % i == 0:
                if i % 2 == 1:
                    counter += 1
                c = num // i
                if i != c and c % 2 == 1:
                    counter += 1
        if num % 2 == 1:
            counter += 1
        return counter

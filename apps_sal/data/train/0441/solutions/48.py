class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        counts = 0
        i = 1
        while True:
            calc = (i*i - i) / 2
            if calc >= n:
                break
            if (n - calc) % i == 0:
                counts += 1
            i += 1
        print((2.2222 % 1))
        return counts


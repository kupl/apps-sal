class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        if n > 10:
            return self.countNumbersWithUniqueDigits(10)
        count = 0
        for i in range(1, n + 1):  # number of digits
            temp = 1
            for j in range(i):
                temp *= 10 - j
            if temp > 10:
                temp = temp // 10 * 9
            count += temp
        return count

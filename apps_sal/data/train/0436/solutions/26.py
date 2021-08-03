class Solution:

    def minDays(self, n: int) -> int:
        mem = {1: 1}

        def calCulatedays(num):
            if not num:
                return 0
            if num in mem:
                return mem[num]
            summ = num
            oneCheck = 0
            if num % 3 == 0:
                oneCheck += 1
                summ = min(calCulatedays(num / 3), summ)
            if num % 2 == 0:
                oneCheck += 1
                summ = min(calCulatedays(num / 2), summ)
            if oneCheck != 2:
                summ = min(calCulatedays(num - 1), summ)
            mem[num] = summ + 1
            return mem[num]
        return calCulatedays(n)

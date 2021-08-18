class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getPowerValue(num):
            num_steps = 0
            while num != 1:
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1
                num_steps += 1
            return num_steps

        powervalues = sorted([(i, getPowerValue(i)) for i in range(lo, hi + 1)], key=lambda x: x[1])
        return powervalues[k - 1][0]

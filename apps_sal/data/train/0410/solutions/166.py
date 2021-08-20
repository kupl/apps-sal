class Solution:

    def core(self, num: int, counter: int) -> int:
        if num == 1:
            return counter
        if num % 2 == 0:
            return self.core(num // 2, counter + 1)
        return self.core(num * 3 + 1, counter + 1)

    def getPowerValue(self, num: int) -> int:
        return self.core(num, 0)

    def generatePowerValues(self, lo: int, hi: int) -> List[int]:
        output = [0]
        if hi == 1:
            return output
        for i in range(2, hi + 1):
            if i % 2 == 0:
                output.append(1 + output[i // 2 - 1])
            else:
                output.append(3 + output[(3 * i + 1) // 4 - 1])
        return output[lo - 1:hi]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        output = []
        for i in range(lo, hi + 1):
            output.append((i, self.getPowerValue(i)))
        output.sort(key=lambda x: (x[1], x[0]))
        return output[k - 1][0]

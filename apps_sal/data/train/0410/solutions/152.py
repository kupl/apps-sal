class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        input = list(range(lo, hi + 1))
        output = []

        def getPower(val, currPower):
            if val == 1:
                output.append(currPower)
                return None
            elif val % 2 == 0:
                val /= 2
                currPower += 1
                getPower(val, currPower)
            else:
                val = 3 * val + 1
                currPower += 1
                getPower(val, currPower)
        outputDict = dict.fromkeys(input, 0)
        for num in input:
            getPower(num, 0)
        for (keys, vals) in enumerate(outputDict.keys()):
            outputDict[vals] = output[keys]
        outputDict = sorted(((value, key) for (key, value) in outputDict.items()))
        return outputDict[k - 1][1]

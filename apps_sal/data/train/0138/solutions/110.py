class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        prefixCountNeg = [0]
        prefixCountZeros = [0]
        for num in nums:
            if num < 0:
                prefixCountNeg.append((prefixCountNeg[-1] + 1) % 2)
            else:
                prefixCountNeg.append(prefixCountNeg[-1])
            if num == 0:
                prefixCountZeros.append(prefixCountZeros[-1] + 1)
            else:
                prefixCountZeros.append(prefixCountZeros[-1])

        m = {'0,0': 0}
        res = 0
        for i in range(len(nums)):
            key = ','.join([str(prefixCountNeg[i + 1]), str(prefixCountZeros[i + 1])])
            if key in m:
                res = max(res, i + 1 - m[key])
            else:
                m[key] = i + 1

        return res

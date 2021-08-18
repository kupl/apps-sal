class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        preSum = [0]
        for val in arr:
            preSum.append(preSum[-1] + val)
        sumMap = {}
        preCands = [sys.maxsize] * len(arr)
        sufCands = [sys.maxsize] * len(arr)
        for i, val in enumerate(preSum):
            if val - target in sumMap:
                sufCands[sumMap[val - target]] = i - sumMap[val - target]
                preCands[i - 1] = i - sumMap[val - target]
            sumMap[val] = i

        prefixSum = [sys.maxsize] * len(arr)
        suffixSum = [sys.maxsize] * len(arr)
        for i, val in enumerate(preCands):
            if i + 1 < len(prefixSum):
                prefixSum[i + 1] = min(preCands[i], prefixSum[i])
        for i, val in reversed(list(enumerate(sufCands))):
            if i + 1 < len(suffixSum):
                suffixSum[i] = min(sufCands[i], suffixSum[i + 1])
            else:
                suffixSum[i] = sufCands[i]

        res = sys.maxsize
        for i in range(len(arr)):
            res = min(res, prefixSum[i] + suffixSum[i])

        return res if res != sys.maxsize else -1

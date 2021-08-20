class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def helper(array):
            if len(array) == 0:
                return 0
            result = 0
            pos = 0
            neg = 0
            for n in array:
                if n > 0:
                    (pos, neg) = (pos + 1, neg + 1 if neg > 0 else 0)
                if n < 0:
                    (pos, neg) = (neg + 1 if neg > 0 else 0, pos + 1)
                result = max(result, pos)
            return result
        arrays = []
        subarray = []
        for n in nums:
            if n == 0:
                idx = 0
                arrays.append(subarray)
                subarray = []
                continue
            subarray.append(n)
        if len(subarray) > 0:
            arrays.append(subarray)
        maxlen = 0
        for (i, array) in enumerate(arrays):
            maxlen = max(maxlen, helper(array))
        return maxlen

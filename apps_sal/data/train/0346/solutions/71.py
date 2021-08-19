class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        aDict = collections.defaultdict(int)
        aDict[0] = 1
        aSum = 0
        result = 0
        for i in nums:
            if i % 2 == 1:
                aSum += 1
            if aSum - k in aDict:
                result += aDict[aSum - k]
            aDict[aSum] += 1
        return result

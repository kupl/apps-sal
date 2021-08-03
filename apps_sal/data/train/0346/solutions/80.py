class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        adict = {0: 1}
        x = 0
        result = 0
        for i in nums:
            if i & 1 != 0:
                x += 1
            if x - k in adict:
                result += adict[x - k]
            adict[x] = adict.get(x, 0) + 1
        return result

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        if not arr or len(arr) == 0:
            return 0
        even = 1
        odd = 0
        cur = 0
        ret = 0
        for a in arr:
            cur = (a + cur)
            if cur % 2 == 0:
                even += 1
                ret += odd
            else:
                odd += 1
                ret += even
            ret = ret % (10 ** 9 + 7)
        return ret

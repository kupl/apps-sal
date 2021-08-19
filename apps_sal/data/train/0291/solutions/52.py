class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ret = 0
        (odds, evens) = (0, 1)
        cur = 0
        for num in arr:
            cur ^= num & 1
            if cur:
                ret += evens
                odds += 1
            else:
                ret += odds
                evens += 1
        return ret % (10 ** 9 + 7)

# Refer to Problem 523 for more info
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        currsum = 0
        d = Counter()
        d[0] = 1
        for i, num in enumerate(A):
            currsum += num
            currsum %= K
            if currsum in d:
                # all the past subarray end points where the remainder is same as the current one will act as starting point for the current subarray so that the total sum is divisible by K
                res += d[currsum]
            d[currsum] += 1
        return res

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        v = {(0, 0): -1}
        neg = 0
        zero = 0
        maxlen = 0
        for i, num in enumerate(nums):
            if num < 0:
                neg = 1 - neg
            if num == 0:
                zero += 1
            if (neg, zero) not in v:
                v[(neg, zero)] = i
            else:
                maxlen = max(maxlen, i - v[(neg, zero)])
        # print(v)
        return maxlen

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        a = [None] + nums
        n = len(a)
        pos = [0] * n
        neg = [0] * n
        for i in range(1, n):
            if a[i] > 0:
                pos[i] = pos[i - 1] + 1
                if neg[i - 1]:
                    neg[i] = neg[i - 1] + 1 # we can extend neg iff it exists
            elif a[i] < 0:
                if neg[i - 1]:
                    pos[i] = neg[i - 1] + 1 # same idea as above
                neg[i] = pos[i - 1] + 1
            else: # a[i] == 0
                pass
        return max(pos)

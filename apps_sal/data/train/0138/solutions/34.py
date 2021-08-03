class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l = []
        neg = []
        index = 0
        max_len = 0
        for num in nums:
            if num == 0:
                index = 0
                if len(neg) % 2 == 1:
                    dist = min(neg[0] + 1, len(l) - neg[-1])
                else:
                    dist = 0
                max_len = max(len(l) - dist, max_len)
                l.clear()
                neg.clear()
            else:
                if num < 0:
                    neg.append(index)
                l.append(num)
                index += 1

        if len(neg) % 2 == 1:
            dist = min(neg[0] + 1, len(l) - neg[-1])
        else:
            dist = 0
        max_len = max(len(l) - dist, max_len)

        return max_len

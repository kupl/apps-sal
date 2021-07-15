class Solution:
    def minOperationsMaxProfit(self, nums: List[int], pos: int, fee: int) -> int:
        if 4*pos <= fee:
            return -1
        ans = cur = 0
        s = sum(nums)
        best = -math.inf
        p = 0
        for i, x in enumerate(nums):
            cur += x
            if cur >= 4:
                p += (4*pos - fee)
                cur -= 4
            else:
                p += (cur * pos - fee)
                cur = 0
            
            if p > best:
                best = p
                ans = i + 1
        res = len(nums)
        while cur > 0:
            res += 1
            if cur >= 4:
                p += (4*pos - fee)
                cur -= 4
            else:
                p += (cur * pos - fee)
                cur = 0
            if p > best:
                best = p
                ans = res
                
        if best <=0:
            return -1
        return ans


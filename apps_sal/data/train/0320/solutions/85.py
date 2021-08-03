class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt1 = 0
        maxcnt0 = 0
        for n in nums:
            cnt0 = 0
            while n > 0:
                if n % 2 == 1:
                    n -= 1
                    cnt1 += 1
                else:
                    n //= 2
                    cnt0 += 1
            maxcnt0 = max(cnt0, maxcnt0)

        return maxcnt0 + cnt1

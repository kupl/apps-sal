class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans, nxt = 0, []
        for num in nums:
            if num & 1:
                num -= 1
                ans += 1
            if num:
                nxt.append(num // 2)
        if nxt:
            ans += 1
        return ans + self.minOperations(nxt)

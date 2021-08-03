class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dic = {}
        cur = 0
        ans = math.inf
        dic[0] = -1

        s = sum(x % p for x in nums) % p

        for i, x in enumerate(nums):
            x %= p
            cur = (cur + x) % p
            t = (cur - s) % p
            dic[cur] = i
            if t in dic:
                ans = min(ans, i - dic[t])

        return -1 if ans == len(nums) else ans

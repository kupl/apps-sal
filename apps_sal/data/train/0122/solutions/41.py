class Solution:

    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return sum(nums)
        pre = [0]
        post = []
        for e in nums:
            pre.append(pre[-1] + e)
            post.append(e)
        post.append(0)
        for i in range(n - 1, -1, -1):
            post[i] = post[i + 1] + nums[i]
        res = 0
        j = n - k
        while j <= n:
            res = max(res, pre[i] + post[j])
            i += 1
            j += 1
        return res

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # self.res = sys.maxsize
        ht = {}
        res = self.dfs(jobDifficulty, d, ht)
        if res == sys.maxsize:
            return -1
        return res
    
    def dfs(self, nums, K, ht):
        if K == 1:
            if len(nums) == 0:
                return sys.maxsize
            return max(nums)
        key = (len(nums), K)
        if key in ht:
            return ht[key]
        res = sys.maxsize
        a = 0
        for i in range(len(nums)):
            a = max(a, nums[i])
            b = self.dfs(nums[i+1:], K-1, ht)
            if a + b < res:
                res = a + b
        ht[key] = res
        return res


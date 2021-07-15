class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        
        res = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_diffs = graph[j]
    
                prev_diff = prev_diffs[diff]
                graph[i][diff] = prev_diff + 1
                res = max(res, graph[i][diff])
        return res + 1

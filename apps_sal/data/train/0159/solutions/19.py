class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp, q = [nums[0]], deque()
        q.append((0,nums[0]))
        res = nums[0]
        for i in range(1, len(nums)):
            while q and i - q[0][0] >k:
                q.popleft()
            cur = nums[i]
            if q:
                cur +=max(q[0][1],0)
            while q and q[-1][1] < cur:
                q.pop()
            q.append((i,cur))
            dp.append(cur)
            res = max(res,cur)
        return res
            
        



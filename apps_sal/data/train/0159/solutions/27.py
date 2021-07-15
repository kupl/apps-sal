class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = []
        res = float('-inf')
        for i in range(len(nums)):
            while q and i-q[0][0] > k:
                q.pop(0)
            temp = nums[i]
            if q and q[0][1] > 0:
                temp += q[0][1]
            res = max(res, temp)
            while q and q[-1][1] <= temp:
                q.pop()
            q.append((i, temp))
        return res

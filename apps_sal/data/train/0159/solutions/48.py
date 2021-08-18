import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = nums.copy()
        q = []
        for i in range(n - 1, -1, -1):
            while q and q[0][1] - i > k:
                heapq.heappop(q)
            if q:
                ans[i] += max(0, -q[0][0])
            heapq.heappush(q, (-ans[i], i))
        return max(ans)

import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minhp = []
        maxhp = []
        i = 0
        ans = 0
        for j, el in enumerate(nums):
            heapq.heappush(minhp, [el, j])
            heapq.heappush(maxhp, [-el, j])
            while -maxhp[0][0] - minhp[0][0] > limit:
                i = min(maxhp[0][1], minhp[0][1]) + 1
                while maxhp[0][1] < i:
                    heapq.heappop(maxhp)
                while minhp[0][1] < i:
                    heapq.heappop(minhp)
            ans = max(ans, j - i + 1)
        return ans

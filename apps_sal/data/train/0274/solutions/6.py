class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        import heapq
        mnq, mxq = [], []
        res = 0
        left = -1
        for right, num in enumerate(nums):
            heapq.heappush(mnq, (num, right))
            heapq.heappush(mxq, (-num, right))
            
            while -mxq[0][0] - mnq[0][0] > limit:
                left = min(mnq[0][1], mxq[0][1])
                while mxq[0][1] <= left:
                    heapq.heappop(mxq)
                while mnq[0][1] <= left:
                    heapq.heappop(mnq)
            res = max(res, right - left)
        return res

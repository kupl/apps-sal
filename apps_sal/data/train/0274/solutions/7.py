class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minh = []
        maxh = []
        start = 0
        ans = 0
        deleted = set()
        for end in range(n):
            x = nums[end]
            heappush(minh, (x, end))
            heappush(maxh, (-x, end))
            while minh and minh[0][1] in deleted:
                heappop(minh)
            while maxh and maxh[0][1] in deleted:
                heappop(maxh)
            while minh and maxh and -maxh[0][0] - minh[0][0] > limit and start <= end:
                deleted.add(start)
                start += 1
                while minh and minh[0][1] in deleted:
                    heappop(minh)
                while maxh and maxh[0][1] in deleted:
                    heappop(maxh)
            ans = max(ans, end - start + 1)
        return ans

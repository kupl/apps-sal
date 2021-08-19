class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        import heapq
        h = []
        heapq.heapify(h)
        largeNum = -10000000000
        ans = largeNum
        for i in range(len(nums)):
            if(i == 0):
                ans = nums[i]
                heapq.heappush(h, (-nums[i], i))
            else:
                b = False
                m, index = heapq.heappop(h)
                while(index < i - k):
                    m, index = heapq.heappop(h)
                heapq.heappush(h, (m, index))
                ans = max(ans, nums[i] - m, nums[i])
                heapq.heappush(h, (min(m - nums[i], -nums[i]), i))
            # print(h)
        # print(ans)
        return ans

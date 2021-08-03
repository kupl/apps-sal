class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        heap = []
        heappush(heap, (- nums[0], 0))
        for i in range(1, n):
            while heap[0][1] < i - k:
                heappop(heap)
            cur = heap[0][0]

            dp[i] = nums[i] + max(- cur, 0)
            heappush(heap, (- dp[i], i))
        # print(dp)
        return max(dp)

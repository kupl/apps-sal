class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        H = []
        N = len(nums)
        for i in range(N):
            s = nums[i]
            heapq.heappush(H, s)
            for j in range(i + 1, N):
                s += nums[j]
                heapq.heappush(H, s)
        for _ in range(left - 1):
            heapq.heappop(H)
        result = 0
        for _ in range(left, right + 1):
            result += heapq.heappop(H)
        return result % (10 ** 9 + 7)

import heapq


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        if not nums:
            return 0
        module = 10 ** 9 + 7
        n = len(nums)
        heap = [[nums[i], i] for i in range(n)]
        heapq.heapify(heap)
        count = 0
        ans = 0
        while heap:
            [val, idx] = heapq.heappop(heap)
            count += 1
            if count > right:
                break
            if count >= left:
                ans += val
            if idx + 1 < n:
                heapq.heappush(heap, [val + nums[idx + 1], idx + 1])
        return ans % module

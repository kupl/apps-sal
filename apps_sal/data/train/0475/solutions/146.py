class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(heap)
        count = 0
        range_sum = 0

        while heap:
            num, index = heapq.heappop(heap)
            count += 1
            if count >= left:
                range_sum += num
            if count == right:
                break
            if index < n - 1:
                heapq.heappush(heap, (num + nums[index + 1], index + 1))

        return range_sum % (10**9 + 7)

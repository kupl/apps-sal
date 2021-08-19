class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums = {}
        for i in arr:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1
        import heapq
        queue = [(nums[i], i) for i in nums]
        heapq.heapify(queue)
        while len(queue) > 0 and k > 0:
            (count, n) = heapq.heappop(queue)
            if k >= count:
                k = k - count
            else:
                count = count - k
                k = 0
                heapq.heappush(queue, (count, n))
        return len(queue)

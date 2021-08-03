class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = Counter(arr)
        nums = [(v, k) for k, v in list(count.items())]
        heapq.heapify(nums)
        for _ in range(k):
            v, k = heapq.heappop(nums)
            if v > 1:
                heapq.heappush(nums, (v - 1, k))
        return len(nums)

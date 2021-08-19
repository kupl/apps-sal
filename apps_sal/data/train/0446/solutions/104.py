class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = [(v, k) for (k, v) in collections.Counter(arr).items()]
        heapq.heapify(count)
        while k > 0:
            k -= heapq.heappop(count)[0]
        return len(count) if k >= 0 else len(count) + 1

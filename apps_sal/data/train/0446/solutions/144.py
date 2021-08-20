class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        pq = [(val, key) for (key, val) in list(count.items())]
        heapq.heapify(pq)
        while pq and k > 0:
            (freq, val) = heapq.heappop(pq)
            if freq <= k:
                k -= freq
            else:
                heapq.heappush(pq, (freq - k, val))
                k = 0
        return len(pq)

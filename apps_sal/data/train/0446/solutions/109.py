class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = [[val, key] for key, val in collections.Counter(arr).items()]
        heapq.heapify(hp)

        while k > 0:
            k -= 1
            hp[0][0] -= 1
            if hp[0][0] == 0:
                heapq.heappop(hp)
            #k -= heapq.heappop(hp)[0]

        return len(hp) + (k < 0)

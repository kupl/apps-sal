class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # heap with key to be count of each number
        d = defaultdict(int)
        for i in arr:
            d[i] += 1

        heap = []
        for key, val in d.items():
            heappush(heap, (val, key))
        if k == 0:
            return len(heap)
        while k > 0:
            if not heap:
                return 0
            count = heappop(heap)[0]
            if k < count:
                res = len(heap) + 1
                break
            elif k == count:

                res = len(heap)
                break
            else:
                k -= count
        return res

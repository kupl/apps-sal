from heapq import heappop, heappush


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = {}
        heap = []
        for elem in arr:
            if elem not in freq_map:
                freq_map[elem] = 0
            freq_map[elem] += 1
        for key in freq_map:
            heappush(heap, (freq_map[key], key))
        while k > 0:
            (count, num) = heappop(heap)
            k -= count
        return len(heap) + 1 if k < 0 else len(heap)

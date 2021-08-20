import heapq


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dictv = {}
        li = []
        for i in arr:
            if i in dictv:
                dictv[i] += 1
            else:
                dictv[i] = 1
        li = []
        for i in dictv:
            heapq.heappush(li, (dictv[i], i))
        for _ in range(k):
            (val, key) = heapq.heappop(li)
            if val > 1:
                heapq.heappush(li, (val - 1, key))
        return len(li)

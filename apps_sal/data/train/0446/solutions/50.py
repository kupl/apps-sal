class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == len(arr):
            return 0
        countDict = dict()
        for x in arr:
            if x not in countDict:
                countDict[x] = 0
            countDict[x] += 1
        from heapq import heappush, heappop, heapify
        minHeap = []
        for x in list(countDict.keys()):
            heappush(minHeap, [countDict[x], x])
        while k > 0:
            if k >= minHeap[0][0]:
                k -= minHeap[0][0]
                heappop(minHeap)
            else:
                k -= minHeap[0][0]
        return len(minHeap)

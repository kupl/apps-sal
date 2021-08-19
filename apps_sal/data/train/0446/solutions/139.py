class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        import heapq
        heap = []
        temp = {}
        for i in arr:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        for key in temp:
            heapq.heappush(heap, (temp[key], key))
        print(heap)
        while heap and k:
            (count, key) = heapq.heappop(heap)
            print((count, key, k))
            if k >= count:
                k -= count
            else:
                return len(heap) + 1
        return len(heap)

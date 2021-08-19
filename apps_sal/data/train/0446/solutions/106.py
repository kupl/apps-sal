class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        import heapq
        heap = []
        for key in counter:
            heapq.heappush(heap, (counter[key], key))

        while (heap and k):
            count, key = heapq.heappop(heap)

            if k >= count:
                k -= count
            else:
                return len(heap) + 1
        return len(heap)

# class Solution(object):
#     def findLeastNumOfUniqueInts(self, arr, k):
#         heap = []
#         count = collections.Counter(arr)
#         for key in count:
#             heapq.heappush(heap, (count[key], key))

#         while(heap and k):
#             count, key = heapq.heappop(heap)
#             if k >= count:
#                 k -= count
#             else:
#                 return len(heap) + 1
#         return len(heap)

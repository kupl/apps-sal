class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        heap = [(-freq, num) for num, freq in list(counter.items())]
        heapq.heapify(heap)
        target = len(arr) // 2
        ans = len(heap)
        while target > 0:
            target += heapq.heappop(heap)[0]
        return ans - len(heap)

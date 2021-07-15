class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = list(zip(efficiency, speed))
        arr.sort(reverse=True)
        counter = 0
        curr_max = 0
        heap = []
        for i in arr:
            curr_max = max(curr_max, i[0] * (counter + i[1]))
            heapq.heappush(heap, i[1])
            counter += i[1]
            if len(heap) > k - 1:
                counter -= heapq.heappop(heap)
        return (curr_max) % ((10 ** 9) + 7)
            


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        temp = []
        for i in range(len(efficiency)):
            temp.append([efficiency[i], speed[i]])
        temp.sort(reverse=True)
        heap = []
        cur_sum = 0
        result = 0
        for i in range(len(temp)):
            heapq.heappush(heap, (temp[i][1], i))
            cur_sum += temp[i][1]
            if len(heap) > k:
                cur_sum -= heapq.heappop(heap)[0]
            result = max(result, cur_sum * temp[i][0])
        return result % (10 ** 9 + 7)

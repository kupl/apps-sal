class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        last_on = 0
        heap = []
        heapq.heapify(heap)
        result = 0
        for i, num in enumerate(light):
            if num == last_on + 1:
                last_on = num
                if not heap:
                    result += 1
                while(heap):
                    top = heapq.heappop(heap)
                    if top == last_on + 1:
                        last_on += 1
                    else:
                        heapq.heappush(heap, top)
                        break
                    if not heap:
                        result += 1
            else:
                heapq.heappush(heap, num)
        return result

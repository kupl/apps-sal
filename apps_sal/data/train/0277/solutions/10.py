class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        h = []
        heapq.heapify(h)
        ret = 0
        for (idx, l) in enumerate(light):
            heapq.heappush(h, -l)
            max_val = -heapq.heappop(h)
            ret += max_val == idx + 1
            heapq.heappush(h, -max_val)
        return ret

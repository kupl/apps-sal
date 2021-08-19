import heapq


class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        q = []
        res = 0
        for num in light:
            heapq.heappush(q, -num)
            if -q[0] == len(q):
                res += 1
        return res

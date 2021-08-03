class Solution:
    # def minTaps(self, n: int, ranges: List[int]) -> int:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        opens, closes, closed = [[] for _ in range(n)], [[] for _ in range(n)], set()
        for i in range(len(ranges)):
            idx = 0
            if i - ranges[i] > 0:
                idx = i - ranges[i]
            if idx < len(opens):
                opens[idx].append(i)
            if i + ranges[i] < n:
                closes[i + ranges[i]].append(i)
        heap, cur_open_tap, res = [], None, 0
        for i in range(n):
            for op in opens[i]:
                heappush(heap, [-(op + ranges[op]), op])
            for cl in closes[i]:
                closed.add(cl)
                if cl == cur_open_tap:
                    cur_open_tap = None
            while cur_open_tap is None:
                if not heap:
                    return -1
                if heap[0][1] in closed:
                    heappop(heap)
                else:
                    cur_open_tap = heap[0][1]
                    res += 1
        return res

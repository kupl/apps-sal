class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        import heapq
        print(len(ranges))
        range_tuples = []
        for (i, val) in enumerate(ranges):
            if val == 0:
                continue
            range_tuples.append((max(0, i - val), min(n, i + val)))
        range_tuples = sorted(range_tuples)
        heap = [(0, 0)]
        for (start_pos, end_pos) in range_tuples:
            while heap and heap[0][0] < start_pos:
                heapq.heappop(heap)
            curr_min_cost = float('inf')
            while heap and heap[0][0] == start_pos:
                cost = heapq.heappop(heap)[1]
                if cost < curr_min_cost:
                    curr_min_cost = cost
            if curr_min_cost == float('inf'):
                if not heap:
                    return -1
            else:
                heapq.heappush(heap, (start_pos, curr_min_cost))
            curr_min_cost = min([a for (_, a) in heap])
            heapq.heappush(heap, (end_pos, curr_min_cost + 1))
        while heap and heap[0][0] < n:
            heapq.heappop(heap)
        min_cost = float('inf')
        while heap and heap[0][0] == n:
            cost = heap[0][1]
            if cost < min_cost:
                min_cost = cost
            heapq.heappop(heap)
        if min_cost == float('inf'):
            return -1
        return min_cost

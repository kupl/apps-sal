from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        data = sorted(list(zip(efficiency, speed)), reverse=True)
        pq = []
        current_eff, total = float('inf'), 0
        answer = 0
        print(data)
        for eff, spd in data:
            current_eff = eff
            total += spd
            heappush(pq, spd)
            if len(pq) > k:
                total -= heappop(pq)
            answer = max(answer, current_eff * total)
        return answer % int(1e9 + 7)

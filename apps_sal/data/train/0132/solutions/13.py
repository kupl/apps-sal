class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        if not days:
            return 0
        total = [float('inf') for _ in range(n)]
        total[0] = min(costs)
        for i in range(1, n):
            curday = days[i]
            total[i] = total[i - 1] + min(costs)
            for j in range(i - 1, -1, -1):
                diff = curday - days[j]
                if diff < 7:
                    if j > 0:
                        total[i] = min(total[i], total[j - 1] + costs[1])
                    else:
                        total[i] = min(total[i], costs[1])
                if diff < 30:
                    if j > 0:
                        total[i] = min(total[i], total[j - 1] + costs[2])
                    else:
                        total[i] = min(total[i], costs[2])
                else:
                    break
        return total[-1]

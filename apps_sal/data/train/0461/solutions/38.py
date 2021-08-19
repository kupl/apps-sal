class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy = defaultdict(set)
        for index, higher in enumerate(manager):
            hierarchy[higher].add(index)  # be careful about what variables you add.
        times = defaultdict(int)

        def computeTotalTime(start):
            if start in times:
                return times[start]
            else:
                answer = 0
                for lower in hierarchy[start]:
                    answer = max(answer, computeTotalTime(lower))
                answer += informTime[start]
                times[start] = answer
                return answer
        return computeTotalTime(headID)

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = collections.defaultdict(set)
        for sub, mag in enumerate(manager):
            subs[mag].add(sub)

        heap, time = [(informTime[headID], headID)], 0
        while heap:
            time = heap[0][0]
            while heap and heap[0][0] == time:
                _, mag = heapq.heappop(heap)
                for sub in subs[mag]:
                    heapq.heappush(heap, (time + informTime[sub], sub))
        return time

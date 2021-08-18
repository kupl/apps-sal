from collections import defaultdict, deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = defaultdict(set)
        zero_value = set([])

        for i in range(len(arr)):
            if arr[i] == 0:
                zero_value.add(i)
            else:
                if i + arr[i] < len(arr):
                    graph[i].add(i + arr[i])
                if i - arr[i] >= 0:
                    graph[i].add(i - arr[i])

        queue = deque([start])
        seen = set([])
        while queue:
            for i in range(len(queue)):
                item = queue.popleft()
                if item in zero_value:
                    return True
                seen.add(item)

                for nei in graph[item]:
                    if nei not in seen:
                        queue.append(nei)

        return False

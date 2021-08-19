class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0
        valueIndex = collections.defaultdict(list)
        for (i, a) in enumerate(arr):
            valueIndex[a].append(i)
        queue = collections.deque([0])
        visited = {0: 0}
        visitedValues = set()
        while queue:
            head = queue.popleft()
            if head == len(arr) - 1:
                return visited[head]
            shortNeighbor = [head - 1, head + 1]
            for neighbor in shortNeighbor:
                if 0 <= neighbor < len(arr) and (not neighbor in visited):
                    visited[neighbor] = visited[head] + 1
                    queue.append(neighbor)
            if arr[head] not in visitedValues:
                visitedValues.add(arr[head])
                for neighbor in valueIndex[arr[head]]:
                    if neighbor not in visited:
                        visited[neighbor] = visited[head] + 1
                        queue.append(neighbor)
        return visited[len(arr) - 1]

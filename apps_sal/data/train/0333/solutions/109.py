class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0
        # construct graph
        valueIndex = collections.defaultdict(list)
        for i, a in enumerate(arr):
            valueIndex[a].append(i)

#         graph = collections.defaultdict(list)
#         for i in range(len(arr)):
#             neighbor = []
#             if i > 0:
#                 neighbor.append(i-1)
#             if i < len(arr) - 1:
#                 neighbor.append(i+1)
#             sameValueIndices = valueIndex[arr[i]]
#             for idx in sameValueIndices:
#                 if idx != i:
#                     neighbor.append(idx)
#             graph[i] = neighbor

        # BFS
        queue = collections.deque([0])
        visited = {0: 0}
        visitedValues = set()
        while queue:
            head = queue.popleft()
            # print(f\"head={head}\")
            if head == len(arr) - 1:
                return visited[head]

            shortNeighbor = [head - 1, head + 1]
            for neighbor in shortNeighbor:
                if 0 <= neighbor < len(arr) and not neighbor in visited:
                    visited[neighbor] = visited[head] + 1
                    queue.append(neighbor)

            if arr[head] not in visitedValues:
                visitedValues.add(arr[head])
                for neighbor in valueIndex[arr[head]]:
                    if neighbor not in visited:
                        visited[neighbor] = visited[head] + 1
                        queue.append(neighbor)

        return visited[len(arr) - 1]

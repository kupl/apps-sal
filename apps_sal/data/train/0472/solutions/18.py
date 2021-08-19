class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = defaultdict(list)
        for i in range(len(arr)):
            if i + arr[i] < len(arr):
                graph[i].append(i + arr[i])
            if i - arr[i] >= 0:
                graph[i].append(i - arr[i])

        def isReachable(s, d, graph):
            # Mark all the vertices as not visited
            visited = [False] * (len(arr))

            # Create a queue for BFS
            queue = []

            # Mark the source node as visited and enqueue it
            queue.append(s)
            visited[s] = True

            while queue:

                # Dequeue a vertex from queue
                n = queue.pop(0)

                # If this adjacent node is the destination node,
                # then return true
                if arr[n] == d:
                    return True

                #  Else, continue to do BFS
                for i in graph[n]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
             # If BFS is complete without visited d
            return False
        return isReachable(start, 0, graph)

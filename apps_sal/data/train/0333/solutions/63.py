class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)
        q = deque([0])
        counter = 0
        visited = [0] * len(arr)
        visited[0] = 1
        while q:
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                if i == len(arr) - 1:
                    return counter
                num = arr[i]
                neighbors = graph[num]
                for neighbor in neighbors:
                    if not visited[neighbor]:
                        q.append(neighbor)
                        visited[neighbor] = 1
                graph.pop(num)
                if i + 1 < len(arr) and not visited[i + 1]:
                    q.append(i + 1)
                    visited[i + 1] = 1
                if i - 1 >= 0 and not visited[i - 1]:
                    q.append(i - 1)
                    visited[i - 1] = 1
            counter += 1



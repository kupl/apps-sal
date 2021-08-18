class Solution:
    def minJumps(self, arr: List[int]) -> int:

        graph = defaultdict(list)
        for i in range(len(arr)):
            graph[arr[i]].append(i)
        visited = set()
        src, dest = 0, len(arr) - 1
        queue = deque()
        queue.append((src, 0))
        visited.add(src)
        while queue:
            vid, step = queue.popleft()
            if vid == dest:
                return step
            nextLayer = [vid - 1, vid + 1] + graph[arr[vid]]
            for v in nextLayer:
                if 0 <= v < len(arr) and v != vid and v not in visited:
                    visited.add(v)
                    queue.append((v, step + 1))
            del graph[arr[vid]]
        return -1

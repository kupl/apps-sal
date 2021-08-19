class Solution:

    def minJumps(self, arr: List[int]) -> int:
        graph = collections.defaultdict(list)
        for (i, val) in enumerate(arr):
            graph[val].append(i)

        def dfs():
            queue = deque()
            queue.append((0, 0))
            seen = {0}
            while queue:
                (i, d) = queue.popleft()
                if i == len(arr) - 1:
                    return d
                for j in [i - 1, i + 1] + graph[arr[i]][::-1]:
                    if 0 <= j < len(arr) and j not in seen and (j != i):
                        seen.add(j)
                        if j == len(arr) - 1:
                            return d + 1
                        queue.append((j, d + 1))
        return dfs()

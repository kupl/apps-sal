class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        else:
            num_indices = defaultdict(list)
            for i in range(len(arr) - 1, -1, -1):
                num_indices[arr[i]].append(i)
            visited = {0}
            queue = deque()
            queue.append((0, 0))
            while queue:
                (i, steps) = queue.popleft()
                for j in [i - 1, i + 1] + num_indices[arr[i]]:
                    if j not in visited and 0 <= j < len(arr):
                        if j == len(arr) - 1:
                            return steps + 1
                        else:
                            queue.append((j, steps + 1))
                            visited.add(j)

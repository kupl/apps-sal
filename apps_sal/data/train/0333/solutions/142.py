class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexes = collections.defaultdict(list)
        for idx, v in enumerate(arr):
            indexes[v].append(idx)
        for key in indexes:
            indexes[key] = [
                v
                for j, v in enumerate(indexes[key])
                if not (
                    1 <= j < len(indexes[key]) - 1
                    and indexes[key][j - 1] == v - 1
                    and indexes[key][j + 1] == v + 1
                )
            ]

        queue, visited = collections.deque([(0, 0)]), set([0])

        while queue:
            idx, jumps = queue.popleft()
            if idx == len(arr) - 1:
                return jumps

            v = arr[idx]
            for j in [idx + 1, idx - 1] + indexes[v][::-1]:
                if 0 <= j < len(arr) and j not in visited:
                    visited.add(j)
                    queue.append((j, jumps + 1))

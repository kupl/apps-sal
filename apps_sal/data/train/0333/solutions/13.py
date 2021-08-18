class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexMap = collections.defaultdict(list)
        for i, a in enumerate(arr):
            indexMap[a].append(i)

        d = deque([(0, 0)])
        distance = 0
        visited = {0}
        while d:
            node, distance = d.popleft()
            if node == len(arr) - 1:
                return distance
            for nei in [node - 1, node + 1] + indexMap[arr[node]][::-1]:
                if 0 <= nei < len(arr) and nei != node and nei not in visited:
                    visited.add(nei)
                    if nei == len(arr) - 1:
                        return distance + 1
                    d.append((nei, distance + 1))

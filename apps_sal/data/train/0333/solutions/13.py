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

        # def bfs():
        #     from collections import deque
        #     Q = deque([(0,0)])
        #     seen = {0}
        #     while Q:
        #         i, d = Q.popleft()
        #         if i==len(arr)-1:return d
        #         for j in [i-1, i+1]+a_i[arr[i]][::-1]:
        #             if 0<=j<len(arr) and j!=i and j not in seen:
        #                 seen.add(j)
        #                 if j==len(arr)-1:return d+1
        #                 Q.append((j,d+1))
        # return bfs()

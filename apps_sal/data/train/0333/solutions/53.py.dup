# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         n = len(arr)
#         if n <= 1:
#             return 0

#         graph = {}
#         for i in range(n):
#             if arr[i] in graph:
#                 graph[arr[i]].append(i)
#             else:
#                 graph[arr[i]] = [i]

#         curs = [0]  # store current layers
#         visited = {0}
#         step = 0

#         # when current layer exists
#         while curs:
#             nex = []

#             # iterate the layer
#             for node in curs:
#                 # check if reached end
#                 if node == n-1:
#                     return step

#                 # check same value
#                 for child in graph[arr[node]]:
#                     if child not in visited:
#                         visited.add(child)
#                         nex.append(child)

#                 # clear the list to prevent redundant search
#                 graph[arr[node]].clear()

#                 # check neighbors
#                 for child in [node-1, node+1]:
#                     if 0 <= child < len(arr) and child not in visited:
#                         visited.add(child)
#                         nex.append(child)

#             curs = nex
#             step += 1

#         return -1

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr or len(arr) == 1:
            return 0

        val_to_idxes = collections.defaultdict(list)
        adj = collections.defaultdict(set)

        for i in range(len(arr)):
            val_to_idxes[arr[i]].append(i)

        # bfs
        # [(idx, dist)]
        q = [(0, 0)]
        visited = {0}
        while q:
            idx, dist = q.pop(0)

            if idx == len(arr) - 1:
                return dist

            visited.add(idx)

            for neighbor in val_to_idxes[arr[idx]]:

                if neighbor in visited:
                    continue

                q.append((neighbor, dist + 1))
                visited.add(neighbor)

                if neighbor == len(arr) - 1:
                    return dist + 1

            if idx - 1 >= 0 and (idx - 1) not in visited:
                q.append((idx - 1, dist + 1))
                visited.add(idx - 1)

            if idx + 1 < len(arr) and (idx + 1) not in visited:
                q.append((idx + 1, dist + 1))
                visited.add(idx + 1)

                if idx + 1 == len(arr) - 1:
                    return dist + 1

            val_to_idxes[arr[idx]] = []

        return -1

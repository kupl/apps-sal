# from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        def dfs():
            queue = deque()  # or we could also write it as deque([])
            queue.append((0, 0))  # start index ,steps(level)
            seen = {0}

            while queue:
                i, d = queue.popleft()
                if i == len(arr) - 1:
                    return(d)

                for j in [i - 1, i + 1] + graph[arr[i]][::-1]:  # not reversing the array will TLE, even though its correct, cause it will again do BFS on ith index instead of trying other ones first
                    if 0 <= j < len(arr) and j not in seen and j != i:
                        seen.add(j)
                        if j == len(arr) - 1:  # again this part is imp otherwise it will TLE
                            return(d + 1)
                        queue.append((j, d + 1))

        return(dfs())

#         q = deque([[0, 0]])
#         d = defaultdict(list)
#         vis = set([0])
#         for i,val in enumerate(arr):
#             d[val].append(i)

#         while q:
#             idx, steps = q.popleft()
#             if idx == len(arr)-1:
#                 return steps
#             for i in d.pop(arr[idx], [])+[idx+1, idx-1]:
#                 if i not in vis and i >= 0:
#                     vis.add(i)
#                     q.append([i, steps + 1])

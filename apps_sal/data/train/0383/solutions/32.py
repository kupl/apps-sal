class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        d = collections.defaultdict(list)
        for init in initial:
            vis = set(initial)
            Q = collections.deque([init])
            while Q:
                infect = Q.popleft()
                for node in range(len(graph[infect])):
                    if graph[infect][node] == 0: continue
                    if node in vis: continue
                    vis.add(node)
                    d[node].append(init)
                    Q.append(node)
        # count the most frequent node
        res = [0] * n
        for key in d:
            if len(d[key]) == 1:
                res[d[key][0]] += 1
        if max(res) == 0: return min(initial)
        return res.index(max(res))
#         def find(x):
#             if x != parents[x]:
#                 parents[x] = find(parents[x])
#             return parents[x]
        
#         def union(x,y):
#             parents[find(x)] = parents[find(y)]
            
#         n = len(graph)
#         parents = list(range(n))    
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if graph[i][j] == 1:
#                     union(i , j)
                    
#         union = collections.Counter(find(i) for i in range(n))
#         malware = collections.Counter(find(i) for i in initial)
        
#         save , res = min(initial) , 0
#         for i in initial:
#             if malware[find(i)] == 1:
#                 if union[find(i)] > save:
#                     save , res = union[find(i)] , i
#                 elif union[find(i)] == save:
#                     res = min(res, i)
                    
#         return res
        


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # if S==T: return 0
        # g = defaultdict(list)
        # q = []
        # t = set()
        # routes = list(map(set, routes))
        # for i, r1 in enumerate(routes):
        #     if S in r1: q.append((i, 1))
        #     if T in r1: t.add(i)
        #     for j in range(i+1, len(routes)):
        #         r2 = routes[j]
        #         if any(s in r2 for s in r1):
        #             g[i].append(j)
        #             g[j].append(i)
        # seen = set(q)
        # while q:
        #     node, jumps = q.pop(0)
        #     if node in t: return jumps
        #     for nxt in g[node]:
        #         if nxt not in seen:
        #             seen.add(nxt)
        #             q.append((nxt, jumps+1))
        # return -1
        
#         st = defaultdict(set)
#         rt = defaultdict(set)
#         for i, route in enumerate(routes):
#             for stop in route:
#                 st[stop].add(i)
#                 rt[i].add(stop)
        
#         q = deque([(S,0)])
#         st_seen = set()
#         rt_seen = set()
#         while q:
#             node, jumps = q.popleft()
#             if node == T: return jumps
#             for r in st[node]:
#                 if r not in rt_seen:
#                     rt_seen.add(r)
#                     for stop in routes[r]:
#                         if stop not in st_seen:
#                             q.append((stop, jumps+1))
#                             st_seen.add(stop)
#         return -1
    
    
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # seen route
        return -1


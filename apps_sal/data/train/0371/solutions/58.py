class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # # 以站点作为node建立graph，站点直接索引下一个站点: time limit exceeded... 怀疑是构建graph太耗时
        #         stop_graph = {}
        #         visited = set()
        #         for rt in routes:
        #             for i in range(len(rt)):
        #                 if rt[i] not in stop_graph: stop_graph[rt[i]] = set(rt[:i] + rt[i+1:])
        #                 else:
        #                     # print(rt[i], set(rt[:i] + rt[i+1:]))
        #                     stop_graph[rt[i]] = stop_graph[rt[i]].union(set(rt[:i] + rt[i+1:]))
        #         #BFS
        #         # visited = set()
        #         # print(stop_graph)
        #         if S == T: return 0
        #         if S not in stop_graph or T not in stop_graph: return -1
        #         cnt = 0
        #         queue = [S]
        #         visited = set(queue)
        #         while queue:
        #             # print(queue)
        #             size = len(queue)
        #             for _ in range(size):
        #                 curr_stop = queue.pop(0)
        #                 for next_stop in stop_graph[curr_stop]:
        #                     if next_stop in visited: continue
        #                     if next_stop == T: return cnt + 1
        #                     queue.append(next_stop)
        #                     visited.add(next_stop)
        #             cnt += 1
        #         else: return -1

        # 以站点作为node建立graph，但用站点索引bus班次，再用Bus索引站点的形式
        # ！！！避免time limit exceed方法必做事项：设两个set()分别记录遍历过的bust stop & bus route，每个stop / route都只应该最多坐一次，这样能避免重复便利stop/route带来的for循环耗时最终导致时间溢出
        graph = {}
        for i in range(len(routes)):
            for st in routes[i]:
                if st not in graph:
                    graph[st] = [i]
                else:
                    graph[st].append(i)

        visited_st = set([S])
        if S == T:
            return 0
        if S not in graph or T not in graph:
            return -1
        queue = graph[S]
        # print(graph[S])
        visited_rt = set(graph[S])
        cnt = 0
        while queue:
            cnt += 1
            size = len(queue)
            for _ in range(size):
                curr_rt_ind = queue.pop(0)
                # if curr_rt_ind in visited: continue
                # visited.add(curr_rt_ind)
                for st in routes[curr_rt_ind]:
                    if st in visited_st:
                        continue
                    if st == T:
                        return cnt
                    visited_st.add(st)
                    for rt_ind in graph[st]:
                        if rt_ind in visited_rt:
                            continue
                        queue.append(rt_ind)
                        visited_rt.add(rt_ind)
        else:
            return -1

#         if S == T: return 0
#         # routes = set(routes)
#         graph = collections.defaultdict(set)
#         for i, r1 in enumerate(routes):
#             for j in range(i+1, len(routes)):
#                 r2 = routes[j]
#                 if any(r in r2 for r in r1):
#                     graph[i].add(j)
#                     graph[j].add(i)

#         seen, targets = set(), set()
#         for node, route in enumerate(routes):
#             if S in route: seen.add(node)
#             if T in route: targets.add(node)

#         queue = [(node, 1) for node in seen]
#         for node, depth in queue:
#             if node in targets: return depth
#             for nei in graph[node]:
#                 if nei not in seen:
#                     seen.add(nei)
#                     queue.append((nei, depth+1))
#         return -1

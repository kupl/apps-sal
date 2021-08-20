class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
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
        visited_rt = set(graph[S])
        cnt = 0
        while queue:
            cnt += 1
            size = len(queue)
            for _ in range(size):
                curr_rt_ind = queue.pop(0)
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

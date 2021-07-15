class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        #build adjacent arrays to represent the graph
        #go through the initial nodes and then do dfs, this could be be timeout.
        d = collections.defaultdict(list)
        for init in initial:
            visit = set(initial)
            q = collections.deque([init])
            while q:
                node = q.popleft()
                for i in range(len(graph[node])):
                    if graph[node][i] == 0 or i in visit:
                        continue
                    visit.add(i)
                    d[i].append(init)
                    q.append(i)
                    
        res = [0] * len(graph)
        for m in d: #这里出错的，是里面的元素而不是索引
        #for m in range(len(d)):
            if len(d[m]) == 1:
                res[d[m][0]] += 1
        if max(res) == 0: return min(initial) #为什么是min(initial)而不是initial[0],题意initial里的值就是index
        return res.index(max(res))

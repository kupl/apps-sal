from collections import defaultdict, Counter


class UF:

    def __init__(self, keys):
        self.uf = {}
        for key in keys:
            self.uf[key] = key

    def find(self, x):
        parent = self.uf[x]
        if parent == x:
            return x
        ret = self.find(parent)
        self.uf[x] = ret
        return ret

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        self.uf[xx] = yy


class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        initial.sort()
        malware = set(initial)
        uf = UF(range(len(graph)))
        neighbors = defaultdict(set)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 0:
                    continue
                elif i in malware and j in malware:
                    continue
                elif i in malware:
                    neighbors[i].add(j)
                elif j in malware:
                    neighbors[j].add(i)
                else:
                    uf.union(i, j)
        components = Counter([uf.find(x) for x in range(len(graph)) if x not in malware])
        infected = defaultdict(set)
        incoming = defaultdict(set)
        for (key, value) in neighbors.items():
            infected[key] = set([uf.find(x) for x in value])
            for component in infected[key]:
                incoming[component].add(key)
        ret = initial[0]
        score = 0
        for mal in initial:
            mal_score = 0
            for component in infected[mal]:
                if len(incoming[component]) == 1:
                    mal_score += components[component]
            if mal_score > score:
                score = mal_score
                ret = mal
        print(components, neighbors, infected, incoming)
        return ret

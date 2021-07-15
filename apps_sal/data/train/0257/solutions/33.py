class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [0.0]*n
        dist[start] = 1.0

        for i in range(n):
            flag = False
            for (a,b), p in zip(edges, succProb):
                if dist[a]==0.0 and dist[b]==0.0:continue
                Max = max(dist[a], dist[b])*p
                if Max > dist[a]:
                    dist[a] = Max
                    flag = True
                if Max > dist[b]:
                    dist[b] = Max
                    flag = True
            if not flag:
                break
                
        return dist[end]

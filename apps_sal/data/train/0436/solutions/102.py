class Solution:
    def minDays(self, N: int) -> int:
        def find_edges(x):
            edges = []
            if x - 1 >= 0:
                edges.append(x - 1)
            if x % 2 == 0:
                edges.append(x // 2)
            if x % 3 == 0:
                edges.append(x // 3)
            return edges

        q = [N]  # make queue
        dist = {N: 0}  # distance dictionary. can use this as visited dictionary too!
        #parent = {N:None}
        while q:
            v = q.pop(0)
            v_edges = find_edges(v)
            for edge in v_edges:
                if not dist.get(edge, False):
                    if edge == 0:
                        return dist[v] + 1
                    dist[edge] = dist[v] + 1
                    #parent[edge] = v
                    q.append(edge)
        return dist[0]

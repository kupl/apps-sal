class Solution:

    def minJumps(self, arr: List[int]) -> int:
        index = {}
        if len(set(arr)) > 10:
            for (ic, val) in enumerate(arr):
                index[val] = index.get(val, []) + [ic]
        else:
            for val in set(arr):
                index[val] = [ic for (ic, v0) in enumerate(arr) if v0 == val]
        neigh = {}
        for (ic, val) in enumerate(arr):
            if ic - 1 >= 0:
                neigh[ic] = neigh.get(ic, []) + [ic - 1]
            if ic + 1 < len(arr):
                neigh[ic] = neigh.get(ic, []) + [ic + 1]
        front = [0]
        visited = {0: 0}
        checkedvalues = set()
        while front != []:
            nf = []
            for u in front:
                val = arr[u]
                for v in neigh.get(u, []):
                    if not v in visited:
                        visited[v] = visited[u] + 1
                        nf.append(v)
                if not val in checkedvalues:
                    for v in index[val] + neigh.get(u, []):
                        if not v in visited:
                            visited[v] = visited[u] + 1
                            nf.append(v)
                checkedvalues.add(val)
            front = nf
        return visited.get(len(arr) - 1, -1)

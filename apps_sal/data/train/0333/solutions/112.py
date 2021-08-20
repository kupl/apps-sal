class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        bfs = [0]
        seen = set()
        seen.add(0)
        G = defaultdict(list)
        for (i, a) in enumerate(arr):
            G[a].append(i)
        step = 0
        while bfs:
            (cur, bfs) = (bfs, [])
            for idx in cur:
                if idx == len(arr) - 1:
                    return step
                for d in (-1, 1):
                    nidx = idx + d
                    if nidx >= 0 and nidx < len(arr):
                        if nidx not in seen:
                            seen.add(nidx)
                            bfs.append(nidx)
                for d in G[arr[idx]]:
                    if d not in seen:
                        if d not in seen:
                            seen.add(d)
                            bfs.append(d)
                G.pop(arr[idx])
            step += 1
        return -1

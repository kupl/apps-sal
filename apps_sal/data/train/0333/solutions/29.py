class Solution:

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        seen = set([0])
        dic = collections.defaultdict(set)
        for (i, num) in enumerate(arr):
            dic[num].add(i)
        bfs = collections.deque([[0, 0]])
        while bfs:
            (ind, c) = bfs.popleft()
            if ind == n - 1:
                return c
            for nind in [ind - 1, ind + 1]:
                if 0 <= nind < n and nind not in seen:
                    bfs.append([nind, c + 1])
                    seen.add(nind)
            for child in dic[arr[ind]]:
                if child not in seen:
                    seen.add(child)
                    bfs.append([child, c + 1])
            dic[arr[ind]] = set()

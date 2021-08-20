class Solution:

    def minJumps(self, arr: List[int]) -> int:
        endpos = len(arr) - 1
        graph = {}
        for (i, n) in enumerate(arr):
            if n not in graph:
                graph[n] = []
            graph[n].append(i)
        curr = set([0])
        hit = set()
        mark = 0
        while curr:
            nxt = set()
            for i in curr:
                hit.add(i)
                if i == endpos:
                    return mark
                if i != 0 and i - 1 not in hit:
                    nxt.add(i - 1)
                if i + 1 not in hit:
                    nxt.add(i + 1)
                if arr[i] in graph:
                    nxt.update([j for j in graph[arr[i]] if i != j and j not in hit])
                    del graph[arr[i]]
            mark += 1
            curr = nxt
        return -1

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n, uf, cs, ones, cache, res = len(arr), list(range(len(arr))), set(), [0] * len(arr), [0] * len(arr), -1

        def find(i):
            while i != uf[i]:
                i = uf[i]
            return i

        def union(nb, cur):
            p = find(nb)
            uf[p] = cur
            cache[cur] += cache[p]
            cache[p] = 0
            if p in cs:
                cs.remove(p)
        for i, v in enumerate(arr):
            l, cur, r = v - 2, v - 1, v
            ones[cur] = 1
            if l >= 0 and ones[l] == 1:
                union(l, cur)
            if r < n and ones[r] == 1:
                union(r, cur)
            cache[cur] += 1
            if cache[cur] == m:
                cs.add(cur)
            if len(cs) > 0:
                res = i + 1
            # print(f'{ones} {cs} {cache} {uf}')
        return res

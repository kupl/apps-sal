class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a': min(a, 2 * (b + c + 1)), 'b': min(b, 2 * (a + c + 1)), 'c': min(c, 2 * (b + a + 1))}
        n = sum(d.values())
        res = []
        for _ in range(n):
            cand = set(['a', 'b', 'c'])
            if len(res) > 1 and res[-1] == res[-2]:
                cand.remove(res[-1])
            tmp = max(cand, key=lambda x: d[x])
            res.append(tmp)
            d[tmp] -= 1
        return ''.join(res)

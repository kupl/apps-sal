class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        p = {}

        def find(i):
            if i not in p:
                p[i] = i
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        for a in A:
            p[a] = a
        for a in A:
            limit = int(math.sqrt(a)) + 1
            for i in range(2, limit):
                if a % i == 0:
                    pa = find(a)
                    pi = find(i)
                    if pa in p and pi in p:
                        p[pa] = p[pi]
                    pa2 = find(a)
                    pi2 = find(a // i)
                    if pa2 in p and pi2 in p:
                        p[pa2] = p[pi2]
        c = {}
        for a in A:
            c[a] = find(a)
        ans = {}
        for (k, v) in list(c.items()):
            if v not in ans:
                ans[v] = 0
            ans[v] += 1
        return max(list(ans.values()))

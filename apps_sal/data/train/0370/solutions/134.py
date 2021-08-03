class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = {}
        rank = {a: 1 for a in A}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    px, py = py, px
                rank[py] += rank[px]
                uf[px] = py

        def primeFactor(x):
            ans = set()
            if not x % 2:
                ans.add(2)
                while not x % 2:
                    x //= 2
            for k in range(3, int(sqrt(x)) + 1, 2):
                if not x % k:
                    ans.add(k)
                while not x % k:
                    x //= k
                if x == 1:
                    break
            if x > 1:
                ans.add(x)
            return ans

        dic = {}
        for a in A:
            for k in primeFactor(a):
                dic.setdefault(k, a)
                union(a, dic[k])
        return max(Counter([find(a) for a in A]).values())

class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            (px, py) = (find(x), find(y))
            if px != py:
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
            if x > 1:
                ans.add(x)
            return ans
        dic = {}
        for i in range(len(A)):
            for k in primeFactor(A[i]):
                dic.setdefault(k, i)
                union(i, dic[k])
        return max(Counter([find(i) for i in range(len(A))]).values())

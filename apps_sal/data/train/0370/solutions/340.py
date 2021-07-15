class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1]*1000001

        def _find(a):
            if parent[a] == -1:
                return a
            parent[a] = _find(parent[a])
            return parent[a]

        def _union(a, b):
            ap = _find(a)
            bp = _find(b)
            if ap != bp:
                parent[bp] = ap

        for a in A:
            for i in range(2, int(sqrt(a)) + 1):
                if a % i == 0:
                    _union(i, a)
                    _union(a, a//i)

        cnt = 0
        tmp = {}
        for a in A:
            ap = _find(a)
            cnt = max(cnt, 1 + tmp.get(ap, 0))
            tmp[ap] = 1 + tmp.get(ap, 0)
        return cnt


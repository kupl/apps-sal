class Solution:

    def largestComponentSize(self, A: List[int], N=100001) -> int:
        m = {}
        P = [i for i in range(N)]
        L = [1] * N

        def find(x):
            P[x] = P[x] if x == P[x] else find(P[x])
            return P[x]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            P[b] = a
            L[a] += L[b]
        for x in A:
            m[x] = x if x not in m else m[x]
            union(m[x], x)
            for i in range(2, floor(sqrt(x)) + 1):
                if x % i:
                    continue
                j = x // i
                m[i] = x if i not in m else m[i]
                union(m[i], x)
                m[j] = x if j not in m else m[j]
                union(m[j], x)
        return max(L)

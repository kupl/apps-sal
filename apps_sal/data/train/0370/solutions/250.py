class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        """
        def gcd(a, b):    
            if b==0:
                return a
            return gcd(b, a%b)
        """

        def find(u):
            if p[u] == -1:
                return u
            p[u] = find(p[u])
            return p[u]

        def union(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                if r[u] > r[v]:
                    p[v] = u
                elif r[u] < r[v]:
                    p[u] = v
                else:
                    p[v] = u
                    r[u] += 1
        '\n        def sieve(x):\n            \n            num = [True]*(x+1)\n            \n            k = 2\n            while k*k<=x:\n                if num[k]:\n                    i = k*k\n                    while i<=x:\n                        num[i] = False\n                        i += k\n                k+=1        \n                \n            for i in range(2, x+1):\n                if num[i]:\n                    pr.append(i)\n            \n        '
        n = len(A)
        m = max(A) + 1
        p = [-1] * m
        r = [0] * m
        for i in range(n):
            factor = 2
            num = A[i]
            while num >= factor * factor:
                if num % factor == 0:
                    num //= factor
                    union(A[i], factor)
                else:
                    factor += 1
            union(A[i], num)
        s = [0] * m
        for i in range(n):
            s[find(A[i])] += 1
        return max(s)
        '\n        # dfs   TLE\n        \n        def gcd(a, b):    \n            if b==0:\n                return a\n            return gcd(b, a%b)\n        \n        def dfs(u):\n            y = 1\n            for v in adj[u]:\n                if not vis[v]:\n                    vis[v] = True\n                    y += dfs(v)\n            \n            return y\n        \n        \n        n = len(A)\n        \n        adj = [ [] for i in range(n) ]\n        \n        for i in range(n):\n            for j in range(i+1,n):\n                if gcd(A[i], A[j])>1:\n                    adj[i].append(j)\n                    adj[j].append(i)\n        \n        \n        \n        res = 0\n        \n        vis = [False]*n\n        \n        for i in range(n):\n            \n            if not vis[i]:\n                vis[i] = True\n                res = max(res, dfs(i))\n        \n        return res\n    '

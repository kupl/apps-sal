class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1] * 100_001  # One more than all values

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xp, yp = find(x), find(y)
            if xp != yp:
                parent[yp] = xp

        for x in A:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    union(i, x)
                    union(x, x // i)
        count = 0
        cache = dict()
        for x in A:
            xp = find(x)
            count = max(count, 1 + cache.get(xp, 0))
            cache[xp] = 1 + cache.get(xp, 0)
        return count

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        graph = dict()
        for a in A:
            graph[a] = list()
        n = len(A)
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                if gcd(a, b) > 1:
                    graph[a].append(b)

        for a in graph.keys():
            print(f'graph[{a}]', graph[a])
        largest = float('-inf')

        def dfs(graph, node, count):
            nonlocal largest
            print('node', node, 'count', count, 'largest', largest)
            if not graph[node]:
                largest = max(largest, count)
                return
            for c in graph[node]:
                dfs(graph, c, count + 1)
        for a in A:
            dfs(graph, a, 1)
        print(largest)
        print('-' * 50)

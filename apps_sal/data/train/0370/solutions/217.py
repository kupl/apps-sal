class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def union(x, y):
            graph[find(x)] = find(y)

        def find(x):
            path = []
            while graph[x] != x:
                path.append(x)
                x = graph[x]
            for n in path:
                graph[n] = x
            return x

        graph = {}
        for i, num in enumerate(A):
            if num not in graph:
                graph[num] = num
            for factor in range(2, int(math.sqrt(num) + 1)):
                if num % factor == 0:
                    for fac in (factor, num // factor):
                        if fac == 0:
                            print(num, fac)
                        if fac in graph:
                            union(num, graph[fac])
                        else:
                            graph[fac] = num

        roots = collections.defaultdict(int)
        for num in A:
            roots[find(num)] += 1
        return max(roots.values())

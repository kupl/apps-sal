from collections import defaultdict


class UnionFind:

    def __init__(self, length):
        self.parent = list(range(length))
        self.size = [1] * length

    def find(self, i):
        if self.parent[i] == i:
            return i
        if self.parent[i] != i:
            return self.find(self.parent[i])

    def union(self, x, y):
        (x_set, y_set) = (self.find(x), self.find(y))
        if x_set == y_set:
            return
        self.parent[x_set] = y_set
        self.size[y_set] += self.size[x_set]
        self.size[x_set] = 0


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        if len(A) <= 0:
            return 0
        "# key: node value\n        # values: list of connected components\n        nodes = defaultdict(list)\n        \n        gcf_cache = {}\n        def greatest_common_factor(a, b):\n            if (a,b) in gcf_cache:\n                return gcf_cache[(a,b)]\n            \n            if (b,a) in gcf_cache:\n                return gcf_cache[(b,a)]\n            \n            # euclidean algo\n            # Everything divides 0  \n            if (a == 0): \n                return b \n            if (b == 0): \n                return a \n\n            # base case \n            if (a == b): \n                return a \n\n            # a is greater \n            if (a > b): \n                gcf = greatest_common_factor(a-b, b)\n                gcf_cache[(a,b)] = gcf\n                gcf_cache[(b,a)] = gcf\n                return gcf\n            gcf = gcd(a, b-a)\n            gcf_cache[(a,b)] = gcf\n            gcf_cache[(b,a)] = gcf\n            return gcf\n        \n        def dfs(node):\n            visited = set()\n            stack = [(node,0)]\n            max_path = -float('inf')\n            while(stack):\n                current_node, current_path = stack.pop()\n                if current_node:\n                    visited.add(current_node)\n                    current_path += 1\n                    max_path = max(max_path, current_path)\n                    neighbors = nodes[current_node]\n\n                    for i in range(len(neighbors)):\n                        if neighbors[i] not in visited:\n                            stack.append((neighbors[i], current_path))\n            return max_path\n        \n        for i in range(len(A)):\n            for j in range(i+1, len(A)):\n                gcf = greatest_common_factor(A[i], A[j])\n                if gcf > 1:\n                    nodes[A[i]].append(A[j])\n                    nodes[A[j]].append(A[i])\n        \n        result = 1\n        for i in nodes.keys():\n            path = dfs(i)\n            print(path)\n            result = max(result, dfs(i))\n        return result"

        def primeFactors(n):
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out
        uf = UnionFind(len(A))
        primeToIndex = {}
        for (i, a) in enumerate(A):
            primes = primeFactors(a)
            for p in primes:
                if p in primeToIndex:
                    uf.union(i, primeToIndex[p])
                primeToIndex[p] = i
        return max(uf.size)

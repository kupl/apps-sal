from math import sqrt
from collections import Counter


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = [i for i in range(len(A))]
        size = [1 for i in range(len(A))]
        primes = {}

        def find_parent(node):
            if node == parent[node]:
                return node
            parent[node] = find_parent(parent[node])
            return parent[node]

        def union(a, b):
            par_a = find_parent(a)
            par_b = find_parent(b)
            parent[par_a] = par_b

        def primes_set(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return primes_set(n // i) | set([i])
            return set([n])
        for (i, num) in enumerate(A):
            pr_set = primes_set(num)
            for q in pr_set:
                primes[q] = primes.get(q, []) + [i]
        for (i, nodes) in list(primes.items()):
            nodes = list(set(nodes))
            for j in range(len(nodes) - 1):
                union(nodes[j], nodes[j + 1])
        return max(Counter([find_parent(i) for i in range(len(A))]).values())

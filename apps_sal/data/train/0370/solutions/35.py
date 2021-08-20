class UnionFind:

    def __init__(self, nodes):
        self.parents = [-1] * len(nodes)
        self.map = {node: idx for (idx, node) in enumerate(nodes)}

    def find(self, node):
        idx = self.map[node]
        orig = idx
        while self.parents[idx] >= 0:
            idx = self.parents[idx]
        (parent, rank) = (idx, abs(self.parents[idx]))
        while self.parents[orig] >= 0:
            temp_parent = self.parents[orig]
            self.parents[orig] = parent
            orig = temp_parent
        return (parent, rank)

    def union(self, n1, n2):
        (idx1, idx2) = (self.map[n1], self.map[n2])
        (parent1, rank1) = self.find(n1)
        (parent2, rank2) = self.find(n2)
        if parent1 == parent2:
            return
        if rank1 >= rank2:
            self.parents[parent1] -= rank2
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] -= rank1
            self.parents[parent1] = parent2

    def get_max_rank(self):
        return abs(min(self.parents))


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        max_num = max(A)
        primes_nodes = collections.defaultdict(set)

        def prime_factors(n):
            original = n
            result = set()
            while n % 2 == 0:
                n = n // 2
                result.add(2)
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    result.add(i)
                    n = n // i
            if n > 2:
                result.add(n)
            return result
        uf_obj = UnionFind(A)
        factor_first_multiple_map = {}
        for node in A:
            p_factors = prime_factors(node)
            for pf in p_factors:
                if pf in factor_first_multiple_map:
                    uf_obj.union(node, factor_first_multiple_map[pf])
                else:
                    factor_first_multiple_map[pf] = node
        return uf_obj.get_max_rank()

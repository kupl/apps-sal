from collections import defaultdict


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def getFactors(n):
            if n == 1:
                return [1]
            factor_set = []
            if n % 2 == 0:
                factor_set.append(2)
                while n % 2 == 0:
                    n = n // 2
            if n > 1:
                for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
                    if n % i == 0:
                        factor_set.append(i)
                        while n % i == 0:
                            n = n // i
                    if n == 1:
                        break
            if n > 2:
                factor_set.append(n)
            return factor_set

        def find(parent, n):
            result = parent[n]
            if result != n:
                parent[n] = find(parent, result)
            return parent[n]

        def union(parent, n1, n2):
            r1 = rank[n1]
            r2 = rank[n2]
            x1 = find(parent, n1)
            x2 = find(parent, n2)
            if x1 != x2:
                if r1 >= r2:
                    parent[x2] = parent[x1]
                    rank[x1] += 1
                else:
                    parent[x1] = parent[x2]
                    rank[x2] += 1
        max_elem = max(A)
        parent = [i for i in range(max_elem + 1)]
        rank = [0] * (max_elem + 1)
        for item in A:
            factor_set = getFactors(item)
            v1 = find(parent, item)
            if v1 == item:
                union(parent, factor_set[0], v1)
                for factor in factor_set[1:]:
                    union(parent, factor_set[0], factor)
        count = defaultdict(int)
        for item in A:
            count[find(parent, item)] += 1
        return max(count.values())

from collections import defaultdict


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1] * 100001

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                parent[p_y] = p_x
        for item in A:
            for i in range(2, int(sqrt(item)) + 1):
                if item % i == 0:
                    union(i, item)
                    union(item, item // i)
        cache = defaultdict(int)
        for i in A:
            p = find(i)
            cache[p] += 1
        return max(cache.values())

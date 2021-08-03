import math


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = dict()

        def find_parent(x):
            if x not in parent:
                parent[x] = -1
                return x

            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]

        def union_num(x, y):
            px = find_parent(x)
            py = find_parent(y)
            if px != py:
                parent[py] = px
            return

        for x in A:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    union_num(i, x)
                    union_num(i, x // i)

        count = 0
        count_ref = dict()
        for x in A:
            p = find_parent(x)
            count_ref[p] = count_ref.get(p, 0) + 1
            count = max(count, count_ref[p])
        return count

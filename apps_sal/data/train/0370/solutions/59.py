class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        (parent, size) = ({x: x for x in A}, {x: 1 for x in A})

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            if b not in parent:
                parent[b] = b
                size[b] = 0
            (x, y) = (find(a), find(b))
            if x != y:
                if size[x] < size[y]:
                    (x, y) = (y, x)
                parent[y] = x
                size[x] += size[y]
        for x in A:
            num = x
            if not x & 1:
                union(x, -2)
                x >>= 1
                while not x & 1:
                    x >>= 1
            i = 3
            while i * i <= x:
                if x % i == 0:
                    union(num, -i)
                    while x % i == 0:
                        x //= i
                i += 2
            if x > 1:
                union(num, -x)
        return max(size.values())

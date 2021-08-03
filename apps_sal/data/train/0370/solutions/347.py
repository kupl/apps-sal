class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        parent = dict()

        def find(x):
            parent.setdefault(x, x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            parent[px] = py

        visited = set()
        graph = collections.defaultdict(set)
        count = 0

        for a in A:
            for fact in range(2, int(sqrt(a)) + 1):
                if a % fact == 0:
                    x = a
                    y = fact
                    z = a // fact

                    px = find(a)
                    py = find(y)
                    pz = find(z)

                    if px != py:
                        union(x, y)
                    if px != pz:
                        union(x, z)

        mem = collections.Counter()
        for item in A:
            p = find(item)
            mem[p] += 1
        maxVal = mem.most_common()
        return(maxVal[0][1])

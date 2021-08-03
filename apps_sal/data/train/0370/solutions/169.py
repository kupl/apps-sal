class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        root = list(range(max(A) + 1))

        def find(i):
            while not root[i] == i:
                root[i] = root[root[i]]  # path compress to reduce test time, since we need to do dfs to get the root, so we can find the current root and set previous to this one, repeat it till get the final root we wanted
                i = root[i]
            return i

        def union(a, i):
            root[find(a)] = root[find(i)]

        for a in A:
            for i in range(2, int(math.sqrt(a)) + 1):
                if not a % i:
                    union(a, i)
                    union(a, a // i)

        # for a in A:
        #     dic[find(a)] += 1
        #     res = max(res, dic[find(a)])
        # return res
        return Counter([find(a) for a in A]).most_common(1)[0][1]

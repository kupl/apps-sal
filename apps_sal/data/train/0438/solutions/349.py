class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:

        def root(x):
            if x == group[x]:
                return x
            group[x] = root(group[x])
            return group[x]

        def same(x, y):
            return root(x) == root(y)

        def unite(x, y):
            nonlocal cnt
            x = root(x)
            y = root(y)
            cnt -= sz[x] == m
            if sz[x] < sz[y]:
                (x, y) = (y, x)
            group[y] = x
            sz[x] += sz[y]
        group = [-1 for i in range(len(arr) + 1)]
        sz = [0 for i in range(len(arr) + 1)]
        ones = [False for i in range(len(arr) + 1)]
        cnt = 0
        latest = -1
        for i in range(len(arr)):
            index = arr[i]
            ones[index] = True
            sz[index] = 1
            group[index] = arr[i]
            if index - 1 >= 1 and ones[index - 1]:
                unite(index - 1, index)
            if index + 1 <= len(arr) and ones[index + 1]:
                unite(index + 1, index)
            if sz[root(index)] == m:
                cnt += 1
            if cnt > 0:
                latest = i + 1
        return latest

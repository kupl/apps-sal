class Solution:

    def __init__(self):
        self.ans = -1

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        sz = [1] * n
        group = [i for i in range(n)]

        def find(i):
            root = i
            while group[root] != root:
                root = group[root]
            while i != root:
                nxt = group[i]
                group[i] = root
                i = nxt
            return root

        def union(i, j):
            root1 = find(i)
            root2 = find(j)
            if sz[root1] > sz[root2]:
                sz[root1] += sz[root2]
                group[root2] = root1
            else:
                sz[root2] += sz[root1]
                group[root1] = root2
        nums = [0] * n
        cnt = 0
        for i in range(n):
            nums[arr[i] - 1] = 1
            if arr[i] - 2 >= 0 and nums[arr[i] - 2] == 1:
                if sz[find(arr[i] - 2)] == m:
                    cnt -= 1
                union(arr[i] - 1, arr[i] - 2)
            if arr[i] < n and nums[arr[i]] == 1:
                if sz[find(arr[i])] == m:
                    cnt -= 1
                union(arr[i] - 1, arr[i])
            if sz[find(arr[i] - 1)] == m:
                cnt += 1
            if cnt:
                self.ans = i + 1
        return self.ans

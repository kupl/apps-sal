# class Solution:
#     def findLatestStep(self, A, m):
#         length = [0] * (len(A) + 2)
#         count = [0] * (len(A) + 1)
#         res = -1
#         for i, a in enumerate(A):
#             left, right = length[a - 1], length[a + 1]
#             length[a] = length[a - left] = length[a + right] = left + right + 1
#             count[left] -= 1
#             count[right] -= 1
#             count[length[a]] += 1
#             if count[m]:
#                 res = i + 1
#         return res        


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        sz, cnt = [0]*n, defaultdict(int)
        res = -2
        parent = [i for i in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            cnt[sz[rx]] -= 1
            cnt[sz[ry]] -= 1
            cnt[sz[rx]+sz[ry]] += 1
            parent[ry] = rx
            sz[rx] += sz[ry]
            return

        for idx, a in enumerate(arr):
            a -= 1
            sz[a] = 1
            cnt[1] += 1
            if a-1 >= 0 and sz[a-1] > 0:
                union(a-1,a)
            if a+1 < n and sz[a+1] > 0:
                union(a,a+1)
            if cnt[m] > 0:
                res = idx
        return res+1

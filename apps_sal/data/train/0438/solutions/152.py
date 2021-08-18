class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        parents = [i for i in range(len(arr) + 1)]
        cnt = [1] * (len(arr) + 1)
        groupCnt = [0] * (len(arr) + 1)
        rank = [0] * (len(arr) + 1)

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                groupCnt[cnt[px]] -= 1
                groupCnt[cnt[py]] -= 1
                cnt[px] = cnt[py] = cnt[px] + cnt[py]
                groupCnt[cnt[px]] += 1
                if rank[px] > rank[py]:
                    parents[py] = px
                elif rank[px] < rank[py]:
                    parents[px] = py
                else:
                    parents[py] = px
                    rank[px] += 1
        visited = [False] * (len(arr) + 1)
        res = -1
        for i, num in enumerate(arr):
            groupCnt[1] += 1
            if num - 1 > 0 and visited[num - 1]:
                union(num, num - 1)
            if num + 1 < len(arr) + 1 and visited[num + 1]:
                union(num, num + 1)
            visited[num] = True
            if groupCnt[m] > 0:
                res = i + 1
        return res

class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        parents = list(range(n + 1))
        ranks = [0] * (n + 1)
        groupCounts = [0] * (n + 1)
        counts = [1] * (n + 1)
        visited = [False] * (n + 1)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                groupCounts[counts[r1]] -= 1
                groupCounts[counts[r2]] -= 1
                counts[r1] = counts[r2] = counts[r1] + counts[r2]
                groupCounts[counts[r1]] += 1
                if ranks[r1] >= ranks[r2]:
                    parents[r2] = r1
                    ranks[r1] += ranks[r2]
                else:
                    parents[r1] = r2
                    ranks[r2] += ranks[r1]
        last = -1
        for (step, index) in enumerate(arr):
            groupCounts[1] += 1
            if index - 1 > 0 and visited[index - 1]:
                union(index, index - 1)
            if index + 1 <= n and visited[index + 1]:
                union(index, index + 1)
            visited[index] = True
            if groupCounts[m]:
                last = step + 1
        return last

from collections import defaultdict


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        counts = defaultdict(int)
        for x in A:
            for y in A:
                counts[x & y] += 1

        def dfs(xy, z, k):
            if k == -1:
                return counts[xy]

            answer = dfs(xy << 1, z, k - 1)
            if (z >> k & 1) == 0:
                answer += dfs(xy << 1 | 1, z, k - 1)
            return answer

        answer = 0
        for z in A:
            answer += dfs(0, z, 16)
        return answer

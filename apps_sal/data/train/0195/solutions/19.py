from collections import defaultdict

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        counts = defaultdict(int)
        for x in A:
            for y in A:
                counts[x & y] += 1
        
        def dfs(z, xy, k):
            if k == -1:
                return counts[xy]
            
            answer = dfs(z, xy << 1, k - 1)
            if (z >> k & 1) == 0:
                answer += dfs(z, (xy << 1 | 1), k - 1)
            return answer
        
        answer = 0
        for z in A:
            answer += dfs(z, 0, 16)
        return answer


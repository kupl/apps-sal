class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        visited = {}

        def recurse(index):
            if index >= len(A):
                return 0
            if index in visited:
                return visited[index]
            mxx = 0
            ans = 0
            for i in range(K):
                if index + i < len(A):
                    mxx = max(mxx, A[i + index])
                    ans = max(ans, mxx * (i + 1) + recurse(i + index + 1))
            visited[index] = ans
            return ans
        return recurse(0)

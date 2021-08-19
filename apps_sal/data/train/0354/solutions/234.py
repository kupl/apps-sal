class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(maxsize=None)
        def DFS(n, i, k):
            if not n:
                return 1
            numSequences = 0
            for j in range(6):
                if not i == j:
                    numSequences += DFS(n - 1, j, 1)
                elif k + 1 <= rollMax[j]:
                    numSequences += DFS(n - 1, j, k + 1)
            return numSequences
        return sum((DFS(n - 1, i, 1) for i in range(6))) % 1000000007

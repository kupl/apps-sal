class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        dp = {-1: 0}
        for j in range(len(A[0])):
            new = defaultdict(lambda: 0)
            for (k, v) in list(dp.items()):
                if k == -1:
                    new[-1] = 0
                    new[j] = 1
                else:
                    if all((ord(A[i][k]) <= ord(A[i][j]) for i in range(len(A)))):
                        new[j] = max(new[j], v + 1)
                    new[k] = max(new[k], v)
            dp = new
        return len(A[0]) - max(dp.values())

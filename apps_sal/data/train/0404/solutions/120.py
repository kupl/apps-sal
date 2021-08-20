class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if len(A) <= K:
            return sum(A)
        A1 = []
        s = 0
        for i in A:
            s += i
            A1.append(s)
        n = len(A)
        last = [A1[i] / (i + 1) for i in range(n)]
        for k in range(1, K):
            cur = [A[0]]
            for i in range(1, n):
                stage_max = 0
                for (j1, j) in enumerate(last[:i]):
                    stage_max = max(stage_max, j + (A1[i] - A1[j1]) / (i - j1))
                cur.append(stage_max)
            last = cur
        return last[-1]

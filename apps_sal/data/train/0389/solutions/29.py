class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        k = int(n / 2)
        dp = [set() for i in range(k + 1)]
        dp[0].add(0)
        for i, v in enumerate(A):
            for j in range(min(i + 1, k), 0, -1):
                for m in dp[j - 1]:
                    dp[j].add(m + v)

        total = sum(A)
        for i in range(1, k + 1):
            if i * total % n == 0:
                if (total * i / n) in dp[i]:
                    return True
        return False

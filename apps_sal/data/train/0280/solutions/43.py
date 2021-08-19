class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        costs = [[0] * (n - i) for i in range(n)]
        for l in range(1, n):
            for start in range(n - l):
                old = costs[start + 1][l - 2] if l > 1 else 0
                costs[start][l] = old + (0 if s[start] == s[start + l] else 1)
        opt = [costs[i][-1] for i in range(n)]
        for ki in range(2, k + 1):
            new_opt = [0] * (n - ki + 1)
            for start in range(len(new_opt)):
                new_opt[start] = min((costs[start][l] + opt[start + l + 1] for l in range(n - start - ki + 1)))
            opt = new_opt
        return opt[0]

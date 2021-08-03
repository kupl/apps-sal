# [] DP
# O(6N * 6T): T: upperbound of rollMax

# f(i, d): number of combinations of res[0~i] if the last number is d
# f(i, ?) = 1 if i == 0
#               d'd d d ... d [d]
#               ? d'd d ... d [d]
#               ? ? d'd ... d [d]
#               ? ? ? d'... d [d]
#               ? ? ? ? ... d'[d]
# f(i, d) = sum{ f(j, d') for j in i-rollMax[d] ~ i-1 for d' in 0~5
#               if i-rollMax[d] >= 0 and d' != d }
#          sum{ f(i-1, d') for any d' if rollMax[d] < i} < no limit
MOD = 1000000007


def memorized(f):
    memo = {}

    def helper(*arg):
        if arg not in memo:
            memo[arg] = f(*arg)
        return memo[arg]
    return helper


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @memorized
        def f(i: int, d: int):
            if i == 0:
                return 1
            if i >= rollMax[d]:
                return sum(f(j, d2) for j in range(i - rollMax[d], i) for d2 in range(6) if d2 != d) % MOD
            else:
                return sum(f(i - 1, d2) for d2 in range(6)) % MOD
        return sum(f(n - 1, d) for d in range(6)) % MOD

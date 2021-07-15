#dp
#f(i) = suffixsum[i] - min(f(i+x) for x in range(1,4))
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = dict()
        def dfs(i):
            if i > N-1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = suffixsum[i] - min([dfs(i+x) for x in range(1, 4)])
            return memo[i]
        N = len(stoneValue)
        suffixsum, acc = [0] * N, 0
        for i, v in enumerate(reversed(stoneValue)):
            acc += v
            suffixsum[~i] = acc
        alice = dfs(0)
        bob = suffixsum[0] - alice
        if alice > bob:
            return 'Alice'
        elif alice == bob:
            return 'Tie'
        else:
            return 'Bob'

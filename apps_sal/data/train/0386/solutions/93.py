class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp = {}
        for c in ['a', 'e', 'i', 'o', 'u']:
            dp[c] = 1
        sources = {}
        sources['a'] = ['e', 'i', 'u']
        sources['e'] = ['a', 'i']
        sources['i'] = ['e', 'o']
        sources['o'] = ['i']
        sources['u'] = ['i', 'o']
        for i in range(2, n + 1):
            next_dp = {}
            for c in ['a', 'e', 'i', 'o', 'u']:
                next_dp[c] = sum((dp[s] for s in sources[c])) % 1000000007
            dp = next_dp
        return sum(dp.values()) % 1000000007

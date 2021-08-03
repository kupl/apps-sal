class Solution:
    def distinctSubseqII(self, S: str) -> int:
        def itertools_appr():
            if not S:
                return 0
            from itertools import combinations
            n = len(S)
            MOD = 1000_000_000 + 7
            l = 0
            for i in range(1, n + 1):
                l += len(set(combinations(S, i))) % MOD
            return l

        def from_soln():
            '''
            Imagine we knew the subsequence count without the last char, dp[-1]
            dp[-1] should be twice of the previous one. However we need to account
            for the presence of the same last char previously.
            S = \"abab\"
            dp[0], with chars upto S[0] = { '', 'a' }
            dp[1], with chars upto S[1] = dp[1] * 2 - subseqs we would have
                double counted. {'', 'a', 'b', 'ab'}
                = 4
            dp[2], with chars upto S[2] = 2*dp[1] - adj for double counting
                {'', 'a', 'b', 'ab'} --> dp[1]
                {'a', 'aa', 'ba', 'aba'} --> dp[1] + 'a'
                'a' is double counted = dp[last['a']] - 1
                = 7
            dp[3], with chars upto S[3] = 2*dp[2] - adjustments for double counting
                {'','a','b','ab','aa','ba','aba'} <-- dp[2]
                {'b','ab','bb','abb','aab','bab','abab'} <-- dp[2] + 'b'
                'b', 'ab' are double counted = dp[last['b']] - 1
                = 14

            dp[k] = 2*dp[k-1] - dp[last[S[k]]] - 1, (1 for '')
            '''
            dp = [1]
            last = {}
            for i, x in enumerate(S):
                dp.append(2 * dp[-1])
                if x in last:
                    dp[-1] -= dp[last[x]]
                last[x] = i
            return (dp[-1] - 1) % (10**9 + 7)
        return from_soln()

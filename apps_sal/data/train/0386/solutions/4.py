class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = dict.fromkeys(('a', 'e', 'i', 'o', 'u'), 1)
        for k in range(1, n):
            dp.update(a=sum(dp[v] for v in ('e', 'i', 'u')),
                      e=sum(dp[v] for v in ('a', 'i')),
                      i=sum(dp[v] for v in ('e', 'o')),
                      o=dp['i'],
                      u=sum(dp[v] for v in ('i', 'o')))
        return sum(dp.values()) % (10 ** 9 + 7)

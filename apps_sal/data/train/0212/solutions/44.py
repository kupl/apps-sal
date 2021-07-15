def prodcount(a):
    dp =defaultdict(int)
    a.sort()
    for i in range(0,len(a)):
        dp[a[i]] = 1
        for j in range(i):
            if a[i]%a[j]==0:
                if a[i]//a[j] == a[j]:
                    dp[a[i]] += (dp[a[j]] *dp[a[i]//a[j]])
                elif dp[a[i]//a[j]]:
                    dp[a[i]] += (dp[a[j]] *dp[a[i]//a[j]])
    return sum(dp.values())% (10**9 + 7)
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        return prodcount(A)

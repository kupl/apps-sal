class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix = [0]
        for a in A:
            prefix.append(prefix[-1] + a)
        @lru_cache(None)
        def soa(i, k):
            if len(prefix) - 1 - i <= k:
                return prefix[-1] - prefix[i]
            elif k == 1:
                return (prefix[-1] - prefix[i]) / (len(prefix) - 1 - i)
            best = 0
            for j in range(i + 1, len(prefix) - (k - 1)):
                best = max(best, (prefix[j] - prefix[i]) / (j - i) + soa(j, k - 1))
            return best
        return soa(0, K)

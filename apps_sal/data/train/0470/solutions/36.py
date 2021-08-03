from math import comb


class Solution:
    def threeSumMulti(self, a: List[int], target: int) -> int:
        counts = Counter(a)
        ans = 0
        for i in list(counts.keys()):
            for j in list(counts.keys()):
                k = target - i - j
                if i == j == k:
                    ans += comb(counts[i], 3)
                elif i == j and j < k:
                    ans += comb(counts[i], 2) * counts[k]
                elif i < j and j == k:
                    ans += counts[i] * comb(counts[k], 2)
                elif i < j < k:
                    ans += counts[i] * counts[j] * counts[k]
        return ans % (10**9 + 7)

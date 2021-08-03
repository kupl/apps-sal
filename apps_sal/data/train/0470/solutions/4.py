class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        cnt, res = collections.Counter(A), 0

        for i in cnt:
            for j in cnt:
                k = target - i - j
                if i == j == k:
                    res += (cnt[i] * (cnt[i] - 1) * (cnt[i] - 2)) // 6
                elif i == j:
                    res += (cnt[i] * (cnt[i] - 1) // 2) * cnt[k]
                elif i < j < k:
                    res += cnt[i] * cnt[j] * cnt[k]
                res = res % (10**9 + 7)
        return res

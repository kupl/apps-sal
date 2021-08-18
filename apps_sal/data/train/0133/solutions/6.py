class Solution:
    def balancedString(self, s: str) -> int:
        if len(s) // 4 != len(s) / 4:
            return -1
        ans, lb, n_cnt = len(s), 0, collections.Counter(s)

        for i, l in enumerate(s):
            n_cnt[l] -= 1
            while lb < len(s) and all(len(s) / 4 >= n_cnt[c] for c in 'QWER'):
                ans = min(ans, i - lb + 1)
                n_cnt[s[lb]] += 1
                lb += 1

        return ans

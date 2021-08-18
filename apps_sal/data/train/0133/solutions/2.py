class Solution:
    def balancedString(self, s: str) -> int:
        if len(s) // 4 != len(s) / 4:
            return -1
        ans, p1, p2, n_cnt = len(s), 0, 0, collections.Counter(s)

        while p1 < len(s):
            n_cnt[s[p1]] -= 1
            while p2 < len(s) and all(len(s) / 4 >= n_cnt[c] for c in 'QWER'):
                ans = min(ans, abs(p1 - p2 + 1))
                n_cnt[s[p2]] += 1
                p2 += 1
            if p2 > p1:
                p1, p2 = p2, p1
            p1 += 1

        return ans

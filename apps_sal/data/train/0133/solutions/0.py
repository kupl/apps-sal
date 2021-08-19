class Solution:
    def balancedString(self, s: str) -> int:
        # minimum window so that outside is possible
        if len(s) // 4 != len(s) / 4:
            return -1
        ans, lb, n_cnt = len(s), 0, collections.Counter(s)

        i = 0
        while i < len(s):
            n_cnt[s[i]] -= 1
            while lb < len(s) and all(len(s) / 4 >= n_cnt[c] for c in 'QWER'):
                ans = min(ans, abs(i - lb + 1))
                if ans == 0:
                    return 0
                n_cnt[s[lb]] += 1
                lb += 1
                # here is actually a swap?
            if lb > i:
                i, lb = lb, i
            i += 1

        return ans

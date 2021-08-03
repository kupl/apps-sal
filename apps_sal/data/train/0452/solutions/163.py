class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        jd_len = len(jd)
        if d > jd_len:
            return -1

        hidp = [0] * jd_len
        hidp[-1] = jd[-1]
        for i in range(jd_len - 2, -1, -1):
            hidp[i] = max(jd[i], hidp[i + 1])

        dp = [{} for i in range(d)]

        def find_min(idx: int, _d: int) -> int:
            cache = dp[_d]
            if idx in cache:
                return cache[idx]

            score = float('inf')
            if _d == 0:
                score = hidp[idx]
            else:
                hi = 0
                for i in range(idx, jd_len - _d):
                    hi = max(hi, jd[i])
                    score = min(score, hi + find_min(i + 1, _d - 1))
            cache[idx] = score
            return score
        res = find_min(0, d - 1)
        return res

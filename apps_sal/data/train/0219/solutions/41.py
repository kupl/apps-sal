class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # ans, cum, seen = 0, 0, {}
        # for i, hour in enumerate(hours):
        #     cum = cum + 1 if hour > 8 else cum - 1
        #     if cum > 0:
        #         ans = i + 1
        #     else:
        #         if cum not in seen:
        #             seen[cum] = i
        #         if cum - 1 in seen:
        #             ans = max(ans, i - seen[cum - 1])
        # return ans

        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res

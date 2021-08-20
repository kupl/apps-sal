from collections import Counter


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        res = n
        if n <= 2:
            return n
        c = set(cnt.values())
        min_c = min(cnt.values())
        max_c = max(cnt.values())
        if len(c) == 2 and (sum([1 for k in cnt if cnt[k] == max_c]) == 1 and max_c == min_c + 1 or (sum([1 for k in cnt if cnt[k] == min_c]) == 1 and min_c == 1)) or (len(c) == 1 and min_c == 1) or len(cnt) == 1:
            return res
        for i in reversed(nums[2:]):
            res -= 1
            cnt[i] -= 1
            if cnt[i] == 0:
                del cnt[i]
            if not cnt:
                return res
            c = set(cnt.values())
            min_c = min(cnt.values())
            max_c = max(cnt.values())
            if len(c) == 2 and (sum([1 for k in cnt if cnt[k] == max_c]) == 1 and max_c == min_c + 1 or (sum([1 for k in cnt if cnt[k] == min_c]) == 1 and min_c == 1)) or (len(c) == 1 and min_c == 1) or len(cnt) == 1:
                return res
        return 2

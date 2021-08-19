from typing import List
import collections
import bisect


class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        d = collections.defaultdict(list)
        summ = 0
        d[0].append(-1)
        delta = sum(nums) % p
        if delta == 0:
            return 0
        for (i, num) in enumerate(nums):
            summ = (summ + num) % p
            d[summ].append(i)
        ans = len(nums)
        for k1 in d:
            k2 = (k1 - delta) % p
            if k2 in d:
                for i in d[k1]:
                    j = bisect.bisect(d[k2], i)
                    if j > 0:
                        ans = min(ans, i - d[k2][j - 1])
        return ans if ans < len(nums) else -1

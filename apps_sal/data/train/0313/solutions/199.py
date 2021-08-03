
from typing import List


def binarysearch(start, end, condition, postprocessing):
    l, r = start, end
    while l < r:
        mid = l + (r - l) // 2
        if condition(mid):
            r = mid
        else:
            l = mid + 1
    return postprocessing(l)


class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        def canMakeBouquet():
            def condition(day):
                count = 0
                curr = 0
                for b_day in bloomDay:
                    has_bloomed = day >= b_day
                    if has_bloomed:
                        curr += 1
                        if curr == k:
                            curr = 0
                            count += 1
                    else:
                        curr = 0

                    if count >= m:
                        return True

                return False

            return condition

        def maybeCantMake(final_day):
            return -1 if not canMakeBouquet()(final_day) else final_day

        return binarysearch(0, max(bloomDay), canMakeBouquet(), maybeCantMake)

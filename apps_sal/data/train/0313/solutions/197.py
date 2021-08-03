
from typing import List


def binarysearch(start, end, condition):
    l, r = start, end
    while l < r:
        mid = l + (r - l) // 2
        if condition(mid):
            r = mid
        else:
            l = mid + 1
    return l


class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

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

        return binarysearch(0, max(bloomDay), canMakeBouquet())

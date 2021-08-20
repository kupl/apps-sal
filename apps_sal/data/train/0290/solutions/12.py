from typing import List
import functools


class Solution(object):

    def minCost(self, n, cuts):

        @functools.lru_cache(None)
        def get_cuts(l, r):
            return [c for c in cuts if c > l and c < r]

        @functools.lru_cache(None)
        def solve(l, r):
            mycuts = get_cuts(l, r)
            if len(mycuts) == 1:
                return r - l
            if len(mycuts) == 0:
                return 0
            minn = 1000000000.0
            for pos in mycuts:
                left_cost = solve(l, pos)
                right_cost = solve(pos, r)
                minn = min(minn, left_cost + right_cost + r - l)
            return minn
        cuts = sorted(cuts)
        return solve(0, n)

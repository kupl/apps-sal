"""
http://codeforces.com/problemset/problem/341/B
"""
from typing import List
from bisect import bisect_right


class Solution:

    def patienceSort(self, a: List[int]) -> int:
        n = len(a)
        piles = [n + 1 for i in range(n)]
        nextPileIdx = 0
        for i in a:
            idx = bisect_right(piles, i, 0, nextPileIdx)
            piles[idx] = i
            if idx >= nextPileIdx:
                nextPileIdx += 1
        return nextPileIdx

    def maxIndependentSetSize(self, a: List[int]) -> int:
        return self.patienceSort(a)


def __starting_point():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    s = Solution()
    print(s.maxIndependentSetSize(a))


__starting_point()

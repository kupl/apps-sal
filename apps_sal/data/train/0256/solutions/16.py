from math import ceil


class Solution:
    def ok(self, piles: List[int], k: int, H: int) -> bool:
        return sum([ceil(piles[i] / k) for i in range(len(piles))]) <= H

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        st = 1
        en = sum(piles)

        ans = en

        while st <= en:
            mid = st + (en - st) // 2

            if self.ok(piles, mid, H):
                ans = mid
                en = mid - 1

            else:
                st = mid + 1

        return ans

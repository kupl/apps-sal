class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        if not n:
            return -1

        def binary_search(l, r):
            nonlocal piles, H
            while l < r:
                mid = (l + r) // 2
                if num_hours(mid) <= H:
                    r = mid
                else:
                    l = mid + 1
            return l

        def num_hours(bananas_per_hour):
            nonlocal piles
            res = 0
            for i in piles:
                if bananas_per_hour >= i:
                    res += 1
                    continue
                res += i // bananas_per_hour
                res += 1 if i % bananas_per_hour else 0
            return res
        return binary_search(1, max(piles))


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

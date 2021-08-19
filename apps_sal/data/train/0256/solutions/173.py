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

        def num_hours(k):
            nonlocal n, piles
            res = 0
            for i in range(n):
                num = piles[i]
                if k >= num:
                    res += 1
                    continue
                res += num // k
                res += 1 if num % k else 0
            return res
        return binary_search(1, max(piles))

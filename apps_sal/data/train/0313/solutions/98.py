class Solution:
    IMPOSSIBLE = -1

#     @staticmethod
#     def canMakeBouquetsOnDay(bloom_day: List[int], m: int, k: int, day: int) -> bool:
#         n = len(bloom_day)
#         bouquets_made = 0
#         i = 0
#         while i < n and bouquets_made < m:
#             j = i
#             while j < n and bloom_day[j] <= day:
#                 j += 1
#             if i == j:
#                 i += 1
#             else:
#                 bouquets_made += (j - i) // k
#                 i = j
#         return bouquets_made >= m

#     def minDays(self, bloom_day: List[int], m: int, k: int) -> int:
#         n = len(bloom_day)
#         if k * m > n:
#             return Solution.IMPOSSIBLE
#         l = min(bloom_day) - 1
#         r = max(bloom_day)
#         # The invariant is it is possible to make k bouquets on day r.
#         while r - l > 1:
#             middle = (l + r) // 2
#             if Solution.canMakeBouquetsOnDay(bloom_day, m, k, middle):
#                 r = middle
#             else:
#                 l = middle
#         return r

    def bouquetsFrom(self, l: int, r: int) -> int:
        return (r - l + 1) // self.k

    def minDays(self, bloom_day: List[int], m: int, k: int) -> int:
        self.k = k
        n = len(bloom_day)
        if k * m > n:
            return Solution.IMPOSSIBLE
        bloom_order = list(range(n))
        bloom_order.sort(key=lambda index: bloom_day[index])
        bloomed = [False for _ in range(n)]
        to_left = [0 for _ in range(n)]
        to_right = [0 for _ in range(n)]
        bouquets_made = 0
        for index in bloom_order:
            bloomed[index] = True
            l = index
            r = index
            if index != 0 and bloomed[index - 1]:
                bouquets_made -= self.bouquetsFrom(
                    to_left[index - 1], to_right[index - 1])
                l = to_left[index - 1]
            if index + 1 != n and bloomed[index + 1]:
                bouquets_made -= self.bouquetsFrom(
                    to_left[index + 1], to_right[index + 1])
                r = to_right[index + 1]
            bouquets_made += self.bouquetsFrom(l, r)
            to_left[l] = to_left[r] = l
            to_right[l] = to_right[r] = r
            if bouquets_made >= m:
                return bloom_day[index]
        return Solution.IMPOSSIBLE

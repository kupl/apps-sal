# class Solution:
#     def maxDistance(self, position: List[int], m: int) -> int:
#         position.sort()

#         def check(d):
#             k = 1
#             pre = position[0]
#             for i in range(1, len(position)):
#                 if position[i] - pre >= d:
#                     k += 1
#                     pre = position[i]
#             return k >= m

#         lo, hi = 0, position[-1] - position[0]
#         while lo < hi:
#             mid = (lo + hi)//2
#             if check(mid):
#                 lo = mid
#             else:
#                 hi = mid - 1

#         return lo

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

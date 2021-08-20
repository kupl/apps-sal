class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def can_finish(k):
            hours = 0
            for pile in piles:
                div = pile // k
                hours += div
                if pile % k:
                    hours += 1
            return hours <= H
        (left, right) = (1, max(piles))
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left


'\n3 6 7 11\n1 2 3 4 5 6 7 8 9 10 11\nmid = 6\nhours = 1+1+2+2 6<=8\nmid = 3\nhours = 1+2+3+4 10<=8\nmid = 4\nhours = 1+2+2+3 8<=8\nmid = 3\nhours = 1+2+3+4 10<=8\nmid = 3\nmid = 4\n\n'

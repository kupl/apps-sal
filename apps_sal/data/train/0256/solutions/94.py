class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def can_finish(k):
            hours = 0
            for pile in piles:
                div = pile//k
                hours += div
                if pile%k:
                    hours += 1
                # print(pile, k, pile//k, pile%k, hours)
            return hours<=H
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right)//2
            if can_finish(mid):
                right = mid
            else:
                left = mid+1
        return left

        
        
'''
3 6 7 11
1 2 3 4 5 6 7 8 9 10 11
mid = 6
hours = 1+1+2+2 6<=8
mid = 3
hours = 1+2+3+4 10<=8
mid = 4
hours = 1+2+2+3 8<=8
mid = 3
hours = 1+2+3+4 10<=8
mid = 3
mid = 4

'''

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        curmaxsight = A[0] - 1
        curmaxpair = 0
        for sight in A[1:]:
            if sight + curmaxsight > curmaxpair:
                curmaxpair = sight + curmaxsight
            if sight > curmaxsight:
                curmaxsight = sight
            curmaxsight -= 1
        return curmaxpair

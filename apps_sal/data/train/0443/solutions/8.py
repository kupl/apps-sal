class Solution:

    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in rating:
            for j in rating[rating.index(i) + 1:]:
                for k in rating[rating.index(j) + 1:]:
                    if i < j < k or k < j < i:
                        cnt += 1
        return cnt

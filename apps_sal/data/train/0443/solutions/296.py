class Solution:

    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for (i, r) in enumerate(rating):
            if i >= len(rating) - 2:
                break
            li = [val for val in rating[i + 1:] if val > r]
            for (j, r2) in enumerate(li):
                li2 = [val for val in li[j + 1:] if val > r2]
                cnt += len(li2)
            li = [val for val in rating[i + 1:] if val < r]
            for (j, r2) in enumerate(li):
                li2 = [val for val in li[j + 1:] if val < r2]
                cnt += len(li2)
        return cnt

from itertools import combinations


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        from itertools import combinations

        dic = {}
        for i, x in enumerate(rating):
            dic[x] = i
        rating.sort()
        cnt = 0
        combinations = list(combinations(rating, 3))

        for comb in combinations:
            if (dic[comb[0]] < dic[comb[1]] and dic[comb[1]] < dic[comb[2]]) or (dic[comb[0]] > dic[comb[1]] and dic[comb[1]] > dic[comb[2]]):

                cnt += 1
        return cnt

        return cnt

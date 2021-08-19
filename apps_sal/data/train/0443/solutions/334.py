from itertools import combinations


class Solution:

    def numTeams(self, rating: List[int]) -> int:
        # Store the index in dictionary
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

        # for i in range(len(rating)-2):
        #     print(dic[rating[i]], dic[rating[i + 1]], dic[rating[i + 2]])
        #     if dic[rating[i]] < dic[rating[i + 1]] and dic[rating[i + 1]] < dic[rating[i+ 2]]:
        #         print(dic[rating[i]], dic[rating[i + 1]], dic[rating[i + 2]])
        #         print((rating[i], rating[i+1], rating[i+2]))
        #         cnt += 1

        # for i in range(len(rating)-1, 1, -1):
        #     if dic[rating[i]] > dic[rating[i -1]] and dic[rating[i - 1]] > dic[rating[i -2]]:
        #         print(dic[rating[i]], dic[rating[i - 1]], dic[rating[i - 2]])
        #         print((rating[i], rating[i-1], rating[i-2]))
        #         cnt += 1

        return cnt

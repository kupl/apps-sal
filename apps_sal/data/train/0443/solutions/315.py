class Solution:

    def numTeams(self, rating: List[int]) -> int:

        def combination(rating, tmp, index, ans, target):
            if len(tmp) == target:
                ans.append(tmp[:])
                return
            for i in range(index, len(rating)):
                if len(tmp) == 2 and (not (tmp[0] > tmp[1] > rating[i] or rating[i] > tmp[1] > tmp[0])):
                    continue
                tmp.append(rating[i])
                combination(rating, tmp, i + 1, ans, target)
                tmp.pop()
        possibles = []
        combination(rating, [], 0, possibles, 3)
        count = 0
        for (a, b, c) in possibles:
            if a < b < c or a > b > c:
                count += 1
        return count

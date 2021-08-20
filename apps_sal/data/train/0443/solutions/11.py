class Solution:

    def numTeams(self, rating: List[int]) -> int:

        def getTeams(k, l, prev=None, asc=True):
            if k > len(l):
                return 0
            if (prev is None) & (k == 1):
                return len(l)
            if k == 1:
                if asc:
                    teamCount = sum([x > prev for x in l])
                else:
                    teamCount = sum([x < prev for x in l])
            else:
                teamCount = 0
                larger_x = True
                if prev is not None:
                    larger_x = l[0] > prev
                if (larger_x == asc) | (prev is None):
                    teamCount += getTeams(k - 1, l[1:], l[0], asc)
                teamCount += getTeams(k, l[1:], prev, asc)
            return teamCount
        return getTeams(3, rating, None, True) + getTeams(3, rating, None, False)

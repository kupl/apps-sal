class Solution:

    def numTeams(self, rating: List[int]) -> int:

        def checkLess(a, b, c):
            return rating[a] < rating[b] < rating[c]

        def checkG(a, b, c):
            return rating[a] > rating[b] > rating[c]
        if len(rating) < 3:
            return 0
        if len(rating) == 3:
            if checkLess(0, 1, 2) or checkG(0, 1, 2):
                return 1
            return 0
        result = 0
        n = len(rating)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if checkLess(i, j, k) or checkG(i, j, k):
                        result += 1
        return result

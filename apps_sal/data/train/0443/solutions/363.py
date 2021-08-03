class Solution:
    def numTeams(self, rating: List[int]) -> int:
        L = len(rating)
        result = 0

        for i in range(1, L - 1):
            pivot = rating[i]
            loL, hiL, loR, hiR = 0, 0, 0, 0
            for j in range(i):
                if rating[j] > pivot:
                    hiL += 1
                else:
                    loL += 1
            for j in range(i + 1, L):
                if rating[j] > pivot:
                    hiR += 1
                else:
                    loR += 1
            result += loL * hiR + loR * hiL

        return result

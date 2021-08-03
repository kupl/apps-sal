class Solution:
    def numTeams(self, rating: List[int]) -> int:
        index = {}

        n = len(rating)
        for i in range(n):
            index[rating[i]] = i
        rating.sort()
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if index[rating[i]] < index[rating[j]]:
                    for k in range(j + 1, n):
                        if index[rating[j]] < index[rating[k]]:
                            count += 1

        rating.sort(reverse=True)
        for i in range(n):
            for j in range(i + 1, n):
                if index[rating[i]] < index[rating[j]]:
                    for k in range(j + 1, n):
                        if index[rating[j]] < index[rating[k]]:
                            count += 1

        return count

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        size = len(rating)
        for idx, val in enumerate(rating):
            for next in range(idx + 1, size):
                if rating[next] > val:
                    new = next + 1
                    while new < size:
                        if rating[new] > rating[next]:
                            count += 1
                        new += 1
                elif rating[next] < val:
                    new = next + 1
                    while new < size:
                        if rating[new] < rating[next]:
                            count += 1
                        new += 1
        return count

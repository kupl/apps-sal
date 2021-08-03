class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        l = []
        x = 0

        while x <= len(rating) - 2:
            y = x + 1
            while y <= len(rating) - 1:
                z = y + 1
                while z < len(rating):
                    if rating[x] < rating[y] and rating[y] < rating[z]:
                        teams += 1
                        l.append([rating[x], rating[y], rating[z]])
                    elif rating[x] > rating[y] and rating[y] > rating[z]:
                        teams += 1
                        l.append([rating[x], rating[y], rating[z]])

                    z += 1
                y += 1
            x += 1

        return teams

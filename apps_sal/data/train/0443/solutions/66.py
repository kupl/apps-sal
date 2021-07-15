class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        num_teams = 0
        greater_than = [0] * n
        less_than = [0] * n
        for left in range(n - 1, -1, -1):
            for right in range(left+1, n):
                if rating[right] > rating[left]:
                    greater_than[left] += 1
                    num_teams += greater_than[right]
                else:
                    less_than[left] += 1
                    num_teams += less_than[right]
        return num_teams
                    


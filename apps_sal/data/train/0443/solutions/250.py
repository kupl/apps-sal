class Solution:
    def _is_valid_team(self, rating: List[int], i: int, j: int, k: int) -> bool:
        if rating[i] < rating[j] and rating[j] < rating[k]:
            return True

        if rating[i] > rating[j] and rating[j] > rating[k]:
            return True

        return False

    def numTeams(self, rating: List[int]) -> int:
        num_teams = 0

        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if self._is_valid_team(rating, i, j, k):
                        num_teams += 1

        return num_teams

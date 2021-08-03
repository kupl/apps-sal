class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        teams = []
        self.select([], 3, True, rating, teams)
        self.select([], 3, False, rating, teams)

        return len(teams)

    def select(self, choice, length, increasing, ratings, teams):
        if len(choice) == length:
            teams.append(list(choice))
            return True

        for i, team in enumerate(ratings):
            selected = None
            if len(choice) == 0:
                selected = team
            elif increasing and choice[-1] < team:
                selected = team
            elif not increasing and choice[-1] > team:
                selected = team

            if selected == None:
                continue

            choice.append(selected)
            res = self.select(choice, length, increasing, ratings[i + 1:], teams)
            choice.pop()

        return False

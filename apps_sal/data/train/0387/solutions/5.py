class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = list(votes[0])
        ranks = {}
        for t in teams:
            ranks[t] = [0] * len(teams)
            for v in votes:
                ranks[t][v.index(t)] -= 1
        return ''.join(t for _, t in sorted(((v, t) for t, v in list(ranks.items()))))

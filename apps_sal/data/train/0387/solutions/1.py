class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = {v: [0] * len(votes[0]) for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1

        sort = sorted(list(count.items()), key=lambda x: (x[1], x[0]))
        ans = ''
        for c, _ in sort:
            ans += c
        return ans

        # return ''.join(sorted(votes[0], key=count.get))

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        '''
        ABC
        ACB
        X 1 2 3
        A 2 0 0
        B 0 1 1
        C 0 1 1
        '''

        mem = {}
        for vote in votes:
            for i in range(len(vote)):
                team = vote[i]
                if team not in mem:
                    mem[team] = [0 for _ in range(len(vote))]
                mem[team][i] += 1

        standings = []
        for k, v in mem.items():
            standings.append(tuple(v) + (-ord(k), k))

        standings.sort(reverse=True)

        res = [s[-1] for s in standings]
        return ''.join(res)

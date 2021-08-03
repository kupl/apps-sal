class Solution:
    def numTeams(self, rating: List[int]) -> int:

        def helper(team, rem):
            if len(team) == 3:
                self.count += 1
                return

            for i in range(len(rem)):
                if len(team) == 1:
                    helper(team + [rem[i]], rem[i:])
                else:
                    if team[-2] < team[-1]:
                        if rem[i] > team[-1]:
                            helper(team + [rem[i]], rem[i:])
                    elif team[-2] > team[-1]:
                        if rem[i] < team[-1]:
                            helper(team + [rem[i]], rem[i:])

        self.count = 0
        for i in range(len(rating)):
            helper([rating[i]], rating[i:])
        return self.count

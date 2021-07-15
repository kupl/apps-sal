class Solution:
    def numTeams(self, rating: List[int]) -> int:
        stack, ans = [], 0
        for r in rating:
            new = [[r]]
            for team in stack:
                if len(team) == 1:
                    new.append(team + [r])
                elif len(team) == 2:
                    if team[0] < team[1] < r or team[0] > team[1] > r:
                        ans += 1
            stack.extend(new)
        return ans


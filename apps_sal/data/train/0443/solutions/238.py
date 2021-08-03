class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = [0]

        def generate(team, pos, method):
            if len(team) == 3:
                count[0] += 1
                return
            else:
                for i in range(pos, n):
                    if team != []:
                        if method == 'i':
                            if rating[i] > team[-1]:
                                generate(team + [rating[i]], i + 1, method)
                            else:
                                continue
                        elif method == 'd':
                            if rating[i] < team[-1]:
                                generate(team + [rating[i]], i + 1, method)
                            else:
                                continue
                    if team == []:
                        generate(team + [rating[i]], i + 1, method)
        generate([], 0, 'i')
        generate([], 0, 'd')
        return count[0]

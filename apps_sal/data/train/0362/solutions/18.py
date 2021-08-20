class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        (res, n, dp, hat2persons) = (0, len(hats), {}, collections.defaultdict(list))
        for (person, arr) in enumerate(hats):
            for hat in arr:
                hat2persons[hat - 1].append(person)
        dp[0] = 1
        for hat in range(40):
            dp_new = dict(dp)
            for person in hat2persons[hat]:
                for (state, cnt) in dp.items():
                    if state & 1 << person == 0:
                        if state | 1 << person not in dp_new:
                            dp_new[state | 1 << person] = cnt
                        else:
                            dp_new[state | 1 << person] += cnt
            dp = dp_new
        return dp[(1 << n) - 1] % (10 ** 9 + 7) if (1 << n) - 1 in dp else 0

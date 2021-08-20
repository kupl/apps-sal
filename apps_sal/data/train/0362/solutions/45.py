class Solution:

    def numberWays(self, hats):
        ppl = len(hats)
        hats_to_ppl = [[] for i in range(41)]
        dp = [[-1 for j in range(2 ** ppl)] for i in range(41)]
        for i in range(ppl):
            for j in hats[i]:
                hats_to_ppl[j].append(i)
        return self.dfs(hats_to_ppl, dp, 1, 0, (1 << ppl) - 1)

    def dfs(self, hats_to_ppl, dp, hat, cur_assignment, all_assignment):
        if cur_assignment == all_assignment:
            return 1
        if hat > 40:
            return 0
        if dp[hat][cur_assignment] != -1:
            return dp[hat][cur_assignment]
        res = self.dfs(hats_to_ppl, dp, hat + 1, cur_assignment, all_assignment)
        for ppl in hats_to_ppl[hat]:
            if cur_assignment >> ppl & 1 == 1:
                continue
            res += self.dfs(hats_to_ppl, dp, hat + 1, cur_assignment | 1 << ppl, all_assignment)
            res %= 10 ** 9 + 7
        dp[hat][cur_assignment] = res
        return res

class Solution:
    def numTeams(self, rating):
        self.count = 0

        def dfs(soldier, idx):
            if len(soldier) == 3:
                if soldier[0] < soldier[1] < soldier[2] or soldier[0] > soldier[1] > soldier[2]:
                    self.count += 1
                return
                # 5 % 3
            for i in range(idx, len(rating)):
                soldier.append(rating[i])
                dfs(soldier, i + 1)
                soldier.pop()
        dfs([], 0)
        return self.count

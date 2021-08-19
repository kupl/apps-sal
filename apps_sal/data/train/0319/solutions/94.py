class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dic = collections.defaultdict(int)
        sums = {-1: 0}
        total = sum(stoneValue)
        for (i, s) in enumerate(stoneValue):
            sums[i] = sums[i - 1] + s
        for i in sums:
            sums[i] = total - sums[i] + stoneValue[i]
        sums.pop(-1)

        def dfs(s=0):
            if s not in dic and s < len(stoneValue):
                dic[s] = sums[s] - min([dfs(s + i + 1) for i in range(3)])
            return dic[s]
        dfs()
        return 'Bob' if total > 2 * dic[0] else 'Alice' if total < 2 * dic[0] else 'Tie'

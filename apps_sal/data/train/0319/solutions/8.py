class Solution:
    def stoneGameIII(self, stns: List[int]) -> str:
        stns.reverse()
        if len(stns) > 1:
            ans = [0, stns[0], stns[1] + abs(stns[0])]
            for i in range(2, len(stns)):
                ans.append(max(stns[i] + stns[i - 1] + stns[i - 2] - ans[-3],
                               stns[i] + stns[i - 1] - ans[-2],
                               stns[i] - ans[-1]))
        else:
            ans = stns
        return 'Alice' if ans[-1] > 0 else 'Tie' if ans[-1] == 0 else 'Bob'

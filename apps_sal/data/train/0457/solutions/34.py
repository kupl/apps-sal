class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        queue = [amount]
        visit = {amount: 0}
        while queue:
            remain = queue.pop(0)
            for c in coins:
                branch = remain - c
                if 0 <= branch not in visit:
                    queue.append(branch)
                    visit.update({branch: visit[remain] + 1})
        return visit.get(0) or -1

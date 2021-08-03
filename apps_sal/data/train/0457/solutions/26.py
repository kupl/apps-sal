'''
coins = [2, 7, 10]
        [4, 9, 12] [9, 14, 17] [12, 17, 20]
amount = 14
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        coins.sort()
        visited = {}
        sums = []
        for coin in coins:
            if coin == amount:
                return 1
            visited[coin] = 1
            sums.append(coin)

        q = []
        q.append((1, sums))
        while q:
            count, sums = q.pop()
            next_sums = []
            for coin in coins:
                for s in sums:
                    current = coin + s
                    if current < amount and current not in visited:
                        visited[current] = 1
                        next_sums.append(current)
                    elif current == amount:
                        return count + 1
                    else:
                        visited[current] = 1
            if next_sums:
                q.insert(0, (count + 1, next_sums))
        return -1

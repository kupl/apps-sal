class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        def bfs():
            q = [(amount, 0)]
            if amount == 0:
                return 0
            seen = set()
            coins.sort(reverse=True)
            print(coins)
            while len(q) > 0:
                (a, ci) = q.pop(0)
                if a in seen:
                    continue
                else:
                    seen.add(a)
                for c in coins:
                    if a - c == 0:
                        return ci + 1
                    if a - c > 0:
                        q.append((a - c, ci + 1))
            return -1

        def dfs():
            if amount == 0:
                return 0
            coins.sort()
            s = [(amount, 0)]
            while len(s) > 0:
                (a, ci) = s.pop()
                for c in coins:
                    if a - c == 0:
                        return ci + 1
                    if a - c > 0:
                        s.append((a - c, ci + 1))
            return -1

        def paste() -> int:
            queue = deque([])
            seen = set()
            queue.append((0, 0))
            while queue:
                (summ, num_coins) = queue.popleft()
                if summ == amount:
                    return num_coins
                for coin in coins:
                    if summ + coin <= amount and summ + coin not in seen:
                        queue.append((summ + coin, num_coins + 1))
                        seen.add(summ + coin)
            return -1
        return paste()

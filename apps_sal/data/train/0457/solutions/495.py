class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #         if not amount:
        #             return 0

        #         min_coins = [0] + [float('inf')] * amount

        #         for i in range(amount + 1):
        #             if min_coins[i] < float('inf'):
        #                 for c in coins:
        #                     if i + c <= amount:
        #                         min_coins[i + c] = min(min_coins[i + c], min_coins[i] + 1)

        #         return min_coins[amount] if min_coins[amount] != float('inf') else -1

        if not amount:
            return 0

        q = deque([amount])
        hs = [False] * amount
        count = 0

        while q:
            l = len(q)
            while l:
                n = q.popleft()
                for c in coins:
                    x = n - c
                    if not x:
                        return count + 1
                    if x > 0 and not hs[x]:
                        hs[x] = True
                        q.append(x)
                l -= 1
            count += 1

        return -1

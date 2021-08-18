class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        que = deque()
        seen = set()
        res = -1

        for coin in coins:
            if coin <= amount:
                que.append(coin)
                seen.add(coin)

        count = 1
        while que:
            prev = len(que)
            while prev > 0:
                cur = que.popleft()
                if cur == amount:
                    return count
                for coin in coins:
                    newamount = cur + coin
                    if newamount not in seen and newamount <= amount:
                        que.append(newamount)
                        seen.add(newamount)
                prev -= 1
            count += 1
        return res

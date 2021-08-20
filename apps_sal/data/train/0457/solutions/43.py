class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        coins.sort()
        coins_set = set(coins)
        if amount in coins_set:
            return 1
        queue = deque([[amount, 0]])
        seen = set()
        processed = set()
        while queue:
            (rem, count) = queue.popleft()
            if rem in seen:
                continue
            seen.add(rem)
            for coin in coins:
                new_rem = rem - coin
                if new_rem == 0:
                    return count + 1
                if new_rem > 0:
                    if new_rem in coins_set:
                        return count + 2
                    if new_rem not in seen and new_rem not in processed:
                        queue.append([new_rem, count + 1])
                        processed.add(new_rem)
        return -1

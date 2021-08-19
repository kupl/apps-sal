class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        queue = collections.deque([(amount, 0)])
        seen = {amount}
        while queue:
            (head, res) = queue.popleft()
            if head == 0:
                return res
            for c in coins:
                new_amount = head - c
                if new_amount > -1 and new_amount not in seen:
                    queue.append((new_amount, res + 1))
                    seen.add(new_amount)
        return -1

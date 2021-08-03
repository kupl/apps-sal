from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        last_winner = 0
        num_wins = 0
        maximum = max(arr)
        nums = deque(arr)
        while num_wins < k:
            pos_0 = nums.popleft()
            pos_1 = nums.popleft()
            winner = max(pos_0, pos_1)
            loser = min(pos_0, pos_1)
            if winner == maximum:
                return maximum
            nums.appendleft(winner)
            if winner == last_winner:
                num_wins += 1
            else:
                num_wins = 1
                last_winner = winner
        return last_winner

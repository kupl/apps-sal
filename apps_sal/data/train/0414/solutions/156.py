from collections import deque
from typing import List


class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k > len(arr):
            return max(arr)
        deck = deque(arr)
        prev_winner = None
        winner = None
        count = 1
        c = 0
        while count != k:
            prev_winner = winner
            (winner, loser) = (max(deck[0], deck[1]), min(deck[0], deck[1]))
            deck.popleft()
            deck.popleft()
            deck.appendleft(winner)
            deck.append(loser)
            if winner == prev_winner:
                count += 1
            else:
                count = 1
            c += 1
        return deck[0]

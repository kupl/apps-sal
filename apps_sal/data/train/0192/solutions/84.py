from typing import List
from collections import deque


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles) == 0:
            return 0

        piles.sort()
        piles_deque = deque(piles)
        my_take = 0

        while len(piles_deque) >= 3:
            alice_take = piles_deque.pop()
            my_take += piles_deque.pop()

            bob_take = piles_deque.popleft()

        return my_take

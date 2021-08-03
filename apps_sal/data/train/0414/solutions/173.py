from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        count = 0
        d = deque(arr)
        if k > len(arr):
            return max(arr)
        while count < k:
            winner = max(d[0], d[1])
            loser = min(d[0], d[1])
            if d[0] == winner:
                count += 1
            else:
                count = 1
            d.popleft()
            d.popleft()
            d.appendleft(winner)
            d.append(loser)
        return d[0]

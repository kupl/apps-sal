class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if arr is None:
            return null
        winCount = 0
        lastWinner = -1
        d = deque(arr)
        while winCount < k:
           # print(lastWinner, d[0], d[1])
            winner = max(d[0], d[1])
            loser = min(d[0], d[1])
            if lastWinner == winner:
                winCount += 1
                if winCount > len(arr):
                    return lastWinner
                d.remove(loser)
                d.append(loser)
                continue
            else:
                winCount = 1
                lastWinner = winner
            d.popleft()
            d.popleft()
            d.appendleft(winner)
            d.append(loser)
        return lastWinner

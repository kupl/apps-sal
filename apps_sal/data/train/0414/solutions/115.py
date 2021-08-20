class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        lastWinner = None
        winCount = 0
        deque = collections.deque(arr)
        while winCount < k:
            firstNum = deque.popleft()
            secondNum = deque.popleft()
            winner = firstNum if firstNum > secondNum else secondNum
            loser = firstNum if firstNum <= secondNum else secondNum
            if lastWinner == winner:
                winCount += 1
            else:
                lastWinner = winner
                winCount = 1
            deque.appendleft(winner)
            deque.append(loser)
        return lastWinner

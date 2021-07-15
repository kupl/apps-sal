class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        index = 0
        q = deque(arr)
        winsSoFar = 0
        currentWinner = None
        def playRound():
            nonlocal currentWinner
            nonlocal winsSoFar
            c1 = q.popleft()
            c2 = q.popleft()
            winner = max([c1, c2])
            looser = min([c1, c2])
            q.append(looser)
            q.appendleft(winner)
            if currentWinner != winner:
                winsSoFar = 1
                currentWinner = winner
            else:
                winsSoFar += 1
            if winsSoFar == k:
                return currentWinner
            return -1
        for i in range(0, len(arr)):
            res = playRound()
            if res != -1:
                return res
        return currentWinner
            


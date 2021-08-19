from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)

        li = deque(arr)
        wins = {ele: 0 for ele in arr}
        found_winner = False
        winnerAll = None

        def simulate():
            nonlocal found_winner
            nonlocal winnerAll
            first = li.popleft()
            second = li.popleft()

            if first > second:
                winner = first
                loser = second
            else:
                loser = first
                winner = second

            li.append(loser)
            li.appendleft(winner)
            wins[winner] += 1
            wins[loser] = 0
            # print(\"winner has won, {} times, \",winner, wins[winner])
            if wins[winner] >= k or wins[winner] == n:
                # print(\"found_winner\", winner)
                found_winner = True
                winnerAll = winner

        while (True):
            if found_winner == True:

                return winnerAll
            # print(li)
            simulate()
            # print(wins, found_winner)
        return winnerAll

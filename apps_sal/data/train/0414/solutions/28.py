from collections import deque
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        
        q = deque(arr)
        
        winner = max(q[0], q[1])
        wins = 1
        if winner == q[0]:
            q.popleft()
            loser = q.popleft()
        elif winner == q[1]:
            loser = q.popleft()
            q.popleft()
            
        q.append(loser)
        while wins < k:
            if winner > q[0]:
                wins += 1
                loser = q.popleft()
            else:
                loser = winner
                winner = q.popleft()
                wins = 1
            q.append(loser)   
        return winner


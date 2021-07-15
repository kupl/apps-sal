class Solution:
    def getWinner(self, A: List[int], K: int) -> int:
        n = len(A)
        dq = collections.deque(A)
        winner = -1
        num_wins = 0
        for _ in range(n):
            x = dq.popleft()
            y = dq.popleft()
            
            if x < y:
                x,y = y,x
            
            if winner == x:
                num_wins += 1
            else:
                winner = x
                num_wins = 1
                
            dq.appendleft(x)
            dq.append(y)
            
            if num_wins == K:
                return winner
        return dq[0]

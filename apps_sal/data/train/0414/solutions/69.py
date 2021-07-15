class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = collections.deque(arr)
        streak = 0
        
        if k >= len(arr):
            return max(arr)
        
        while True:
            player = q.popleft()
            while player > q[0] and streak < k:
                opp = q.popleft()
                q.append(opp)
                streak += 1
            if streak == k:
                return player
            streak = 1
            q.append(player)
        


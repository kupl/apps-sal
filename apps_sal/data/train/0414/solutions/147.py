class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        consecutive = 0
        q = deque(arr)
        winner = None
        while consecutive < k and consecutive < len(arr):
            if q[0] < q[1]:
                end = q.popleft()
                start = q.popleft()
            else:
                start = q.popleft()
                end = q.popleft()
            q.appendleft(start)
            q.append(end)
            if q[0] != winner:
                consecutive = 0
                winner = q[0]
            consecutive += 1
        return winner

from collections import deque


class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        cnt = 0
        if k > len(arr):
            return max(arr)
        while True:
            a = q.popleft()
            b = q.popleft()
            if a > b:
                q.appendleft(a)
                q.append(b)
                cnt += 1
            else:
                q.appendleft(b)
                q.append(a)
                cnt = 1
            if cnt >= k:
                return max(a, b)

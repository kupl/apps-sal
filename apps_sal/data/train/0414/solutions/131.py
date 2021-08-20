from collections import deque, defaultdict


class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        d = defaultdict(int)
        while True:
            a = q.popleft()
            b = q.popleft()
            if a > b:
                (a, b) = (b, a)
            d[b] += 1
            q.appendleft(b)
            q.append(a)
            if d[b] == k or d[b] > len(arr) + 2:
                return b

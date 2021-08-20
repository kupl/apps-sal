class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        que = deque(sorted(piles)[::-1])
        res = 0
        while len(que) > 2:
            que.popleft()
            res += que.popleft()
            que.pop()
        return res

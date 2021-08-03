from functools import lru_cache


@lru_cache(maxsize=None)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        A = piles
        Ans = {}

        def hello(st, end, turn):
            if st > end:
                return 0
            if Ans.get((st, end), None) != None:
                return Ans[(st, end)]
            if turn % 2 == 0:
                t = max(A[st] + hello(st + 1, end, turn + 1), A[end] + hello(st, end - 1, turn + 1))
                Ans[(st, end)] = t
                return t
            else:
                t = min(hello(st + 1, end, turn + 1) - A[st], hello(st, end - 1, turn + 1) - A[end])
                Ans[(st, end)] = t
                return t
        t = hello(0, len(A) - 1, 0)
        return t > 0

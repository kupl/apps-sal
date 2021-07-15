from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        A = piles
        @lru_cache(maxsize=None)
        def hello(st,end,turn):
            if st > end:
                return 0
            if turn%2 == 0:
                return max(A[st]+hello(st+1,end,turn+1),A[end]+hello(st,end-1,turn+1))
            else:
                return min(hello(st+1,end,turn+1)-A[st],hello(st,end-1,turn+1)-A[end])
        t = hello(0,len(A)-1,0)
        return t > 0

from functools import lru_cache
class Solution(object):
    def stoneGameIII(self, Values):
        N = len(Values)
        @lru_cache(None)
        def dp(i):
            if i>=N:
                return (0,0)
            if i == N-1:
                return (Values[-1], 0)
            one, two, three = -float('inf'), -float('inf'), -float('inf')
            one = (Values[i]+dp(i+1)[1], dp(i+1)[0])
            if i< N-1:
                two =(Values[i]+Values[i+1]+dp(i+2)[1], dp(i+2)[0])
                one = max(one, two)
            if i<N-2:
                three = (Values[i]+Values[i+1]+Values[i+2]+dp(i+3)[1], dp(i+3)[0])
                one = max(one, three)
            return one
        res = dp(0)
        return 'Alice' if res[0]>res[1] else 'Bob' if res[1]>res[0] else 'Tie'



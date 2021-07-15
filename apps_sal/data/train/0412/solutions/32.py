class Solution:
    def numRollsToTarget(self, k: int, f: int, target: int) -> int:
        d = {}
        def h(x,t):
            v = (x,t)
            if v in d:
                return d[v]
            if x == 0 and t == 0:
                return 1
            if x == 0 or t == 0:
                return 0
            s = 0
            for i in range(1,f+1):
                s+=h(x-1,t-i)
            d[v] = s
            return s
        x = h(k,target)
        return x%(10**9+7)

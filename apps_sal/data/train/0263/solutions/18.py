class Solution:
    def knightDialer(self, n: int) -> int:
        d = {1:(6, 8), 2:(7, 9), 3:(4,8), 4: (0, 3, 9), 5:(), 6: (0, 1, 7), 7:(2, 6), 8:(1, 3), 9:(2, 4), 0:(4,6)}
        prev = [1] * 10
        
        for dial in range(n - 1):
            nex = [0] * 10
            for curNum in range(10):
                for nexNum in d[curNum]:
                    nex[nexNum] = (nex[nexNum] + prev[curNum]) % (10**9+ 7)
            prev = nex [:]
        return sum(prev)%(10**9+ 7)

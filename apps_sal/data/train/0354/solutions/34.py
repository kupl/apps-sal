class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        if n == 0:
            return 0
        hist = [[0 for _ in range(rollMax[i])] for i in range(6)]
        for i in range(6):
            hist[i][0] = 1
        
        for i in range(n-1):
            new = [[0 for _ in range(rollMax[i])] for i in range(6)]
            for j in range(6):
                s = sum(sum(e) for idx, e in enumerate(hist) if idx != j)
                new[j][0] = s
                for rep in range(1, rollMax[j]):
                    new[j][rep] = hist[j][rep-1]
            hist = new
        
        return sum(sum(e) for e in hist) % (1000000007)

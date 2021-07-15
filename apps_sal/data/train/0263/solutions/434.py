class Solution:
    def knightDialer(self, n: int) -> int:
        dp = {(0,0):1, (0,1):1, (0,2):1, 
              (1,0):1, (1,1):1, (1,2):1, 
              (2,0):1, (2,1):1, (2,2):1, 
              (3,1):1}
        for x in range(1, n):
            temp = {}
            for r in range(4):
                for c in range(3):
                    if (r == 3 and c == 0) or (r==3 and c == 2):
                        continue
                    sm = 0
                    for i in (1,-1):
                        for j in (2, -2):
                            sm = sm + dp.get((r+i, c+j), 0) + dp.get((r+j, c+i), 0)
                    temp[(r,c)] = sm
            dp = temp
        return sum(dp.values())%(10**9 + 7)      


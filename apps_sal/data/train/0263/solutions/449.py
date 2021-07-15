class Solution:
    def knightDialer(self, n: int) -> int:
        keyboard = [[0] * 3 for _ in range(4)]
        k = 1
        for i in range(3):
            for j in range(3):
                keyboard[i][j] = k
                k+=1
        keyboard[-1][0] = -1
        keyboard[-1][-1] = -1
        
        mod = 10**9 + 7
        count = [[1] * 3 for _ in range(4)]
        count[-1][0] = 0
        count[-1][-1] = 0
        moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        for k in range(n - 1):
            tmp_count = [[0] * 3 for _ in range(4)]
            for i in range(4):
                for j in range(3):
                    if keyboard[i][j] < 0 :
                        continue
                    for mv in moves:
                        x = i + mv[0]
                        y = j + mv[1]
                        if 0<=x<4 and 0<=y<3 and keyboard[x][y]>=0:
                            tmp_count[x][y] = (tmp_count[x][y] + count[i][j]) % mod
                            
            count = tmp_count
        num_count = 0
        for r in count:
            num_count = (num_count + sum(r)) % mod
        return num_count 

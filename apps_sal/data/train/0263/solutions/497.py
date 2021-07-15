class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        
        pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
        dirs = [[-1, -2], [-2, -1], [1, -2], [2, -1], [-1, 2], [-2, 1], [1, 2], [2, 1]]
        
        memo = dict()
        for i in range(10):
            memo[str(i)] = [0 for j in range(n + 1)]
            memo[str(i)][1] = 1
            
        for j in range(2, n + 1):
            for r in range(4):
                for c in range(3):
                    number = pad[r][c]
                    if number == '*' or number == '#':
                        continue
                    memo[number][j] = 0
                    for dir0 in dirs:
                        x = r + dir0[0]
                        y = c + dir0[1]
                        if x < 0 or x >= 4 or y < 0 or y >= 3 or pad[x][y] == '*' or pad[x][y] == '#':
                            continue
                            
                        parent = pad[x][y]
                        memo[number][j] += memo[parent][j - 1]
        
        res = 0
        for i in range(10):
            number = str(i)
            res += memo[number][n]
        return res % 1_000_000_007
                        
        
        
# Idea:     use 2D dp array memo[10][n + 1] to store the number of distinct phone numbers
#           memo[i][0] = 0
#           memo[i][j] = sum(memo[parent][j - 1])
#           Res = sum(memo[i][n])
# Time:     O(n)
# Space:    O(n)


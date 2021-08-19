class Solution:
    def countOrders(self, n: int) -> int:
        '''
        # Notes:
            example n = 3
                                P1         P2     P3 
                             P2    P3   D1
                        P3   D1  D2
                     D1  D2 D3
                  D2  D3
        # Approach:
            Dynamic Programming
            opt[i][j]   i represents how many delivery are holding
                        j represents how many remaining delivery
                        output = opt[0][n]

                                OPT[0][3]
                                3*OPT[1][2]
                        1*OPT[0][2]        2*OPT[2][1]
                        2*OPT[1][1]     2*OPT[1][1]  1*OPT[3][0]
                    1*OPT[0][1] 1*OPT[2][0]

            OPT[i][j] = i*opt[i-1][j] + j*opt[i+1][j-1]

        '''
        opt = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for j in range(n + 1):
            for i in range(n + 1):
                if j == n:
                    opt[i][j] = j * opt[i + 1][j - 1]
                    return opt[0][n] % (pow(10, 9) + 7)
                if i == 0 and j == 0:
                    continue
                if i == 0 and j == 1:
                    opt[i][j] = 1
                    continue
                if i == 1 and j == 0:
                    opt[i][j] = 1
                    continue
                if i == 0:
                    opt[i][j] = j * opt[i + 1][j - 1]
                elif j == 0:
                    opt[i][j] = i * opt[i - 1][j]
                else:
                    if i + j > n:
                        break
                    opt[i][j] = i * opt[i - 1][j] + j * opt[i + 1][j - 1]

        # return opt[0][n] % (pow(10, 9)+7)

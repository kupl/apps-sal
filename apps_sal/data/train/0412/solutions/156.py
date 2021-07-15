class Solution:
    def numRollsToTarget(self, N: int, faces: int, total: int) -> int:
        DP = {}
        DP[0] = [0] * (total+1)
        DP[1] = [0] + [1]*(faces) + [0] *(total-faces)

        for die in range(2,N+1):
            DP[die] = [0] * (total+1)
            for i in range(1,total+1):#the subtotal
                count  = 0
                for j in range(1,faces+1):#this die's contribution
                    if (i-j) >= 1 and DP[die-1][i-j] > 0:
                        if die==2:
                            print((i,j))
                        count+= DP[die-1][i-j]
                DP[die][i] = count
                print(count)
        ans = DP[N][total]
        return ans %(10**9 + 7)


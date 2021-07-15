class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        memo = [1]*10
        for i in range(n-1):
            memonext = [0]*10
            for j in range(10):
                for m in moves[j]:
                    memonext[m] += memo[j]
                    #print(memonext,m)
            for j in range(10):
                memo[j] = memonext[j]
            #print(memo)
        return sum(memo) % (10**9 + 7)

class Solution:
    def knightDialer(self, N: int) -> int:
        #OPT(i, j) = number of numbers you can dial with j hops reaching i
        #k - possible places I could have come from
        #OPT(i, j) = SUM(OPT(k, j-1))
        #base cases
        #if j = 0, then 0
        #if i = 5, j = j, then OPT(i, j) = 0
        jumps = dict({1:[8,6], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3],9:[2,4], 0:[4,6]})
        table = [[0] * N for i in range(10)]
        for j in range(N):
            for i in range(10):
                if j == 0:
                    table[i][0] = 1
                elif j == 1:
                    table[i][j] = len(jumps[i])
                else:
                    kList = jumps[i]
                    for k in kList:
                        table[i][j] += table[k][j-1]
        res = 0
        for i in range(len(table)):
            res = (res +table[i][-1])%(10**9 + 7)
        return res
        


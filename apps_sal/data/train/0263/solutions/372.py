class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD = 10**9 + 7
        poss = {}
        poss[1] = [6,8]
        poss[2] = [7,9]
        poss[3] = [4,8]
        poss[4] = [3,9,0]
        poss[5] = []
        poss[6] = [1,7,0]
        poss[7] = [2,6]
        poss[8] = [1,3]
        poss[9] = [2,4]
        poss[0] = [4,6]
        
        
        def helper(numb,i):
            # print('numb is ', numb)
            # print('at i ',i)
            if i == n:
                return 1
            if (numb,i) in mem:
                return mem[(numb,i)]
            out= 0
            child = poss[numb]
            nchild = len(child)
            for j in range(nchild):
                val = child[j]
                out += helper(val,i+1)
                out = out % MOD
            mem[(numb,i)] = out 
            return out
        res = 0
        mem = {}
        for i in range(10):
            # print('starting at ',i)
            res += helper(i,1)
        return res % MOD

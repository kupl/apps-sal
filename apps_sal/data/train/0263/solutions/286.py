import numpy as np


class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1: return 10
        def fast_power(a,m):

            res=np.identity(10,int)
            for bit_idx,bit in enumerate(reversed(bin(m)[2:])):
                if bit_idx==0:
                    cur=a
                else:
                    cur=np.mod(np.dot(cur,cur),10**9+7)
                if bit == '1':
                    res=np.mod(np.dot(res,cur),10**9+7)
            return res

        gh = {}
        gh[0] = [4, 6]
        gh[1] = [6, 8]
        gh[2] = [7, 9]
        gh[3] = [4, 8]
        gh[4] = [0,3, 9]
        gh[5] = []
        gh[6] = [0, 1, 7]
        gh[7] = [2, 6]
        gh[8] = [1, 3]
        gh[9] = [2, 4]
        t = []
        for u in gh:
            
            if u != 5:
                row = 0
                for v in gh[u]:
                    row = row^(1 << v)
                row = list(bin(row)[2:])
                row.reverse()
                
                row = list([int(x) for x in row])
                row.extend([0] * (10 - len(row)))
                t.append(row)
            else:
                t.append([0] * 10)
        t = np.array(t,dtype=int)
        
        ans = sum(np.mod(np.dot(fast_power(t, n - 1), np.ones(10,dtype=int)),10**9+7)) % (10**9+7)
        return ans







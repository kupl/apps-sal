class Solution:
    def knightDialer(self, n: int) -> int:
        
        k = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        
        mem = {}
        def count(i, j):
            if j > n: return 0
            if j == n: return 1
            if (i, j) in mem: return mem[i, j]
            
            cc = 0
            for l in k[i]:
                cc += count(l, j + 1)
            
            mem[i, j] = cc % (10 ** 9 + 7)
            return mem[i, j]
        
        
        return sum(count(i, 1) for i in range(10)) % (10 ** 9 + 7)


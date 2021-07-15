class Solution:
    def knightDialer(self, n: int) -> int:
        memo = {}
        return sum(self.hopper(i, n-1, memo) for i in range(10)) % (10 ** 9 + 7)
    
    def hopper(self, cur_ind, hops_left, memo):
        if hops_left == 0:
            return 1
        if (cur_ind, hops_left) in memo:
            return memo[(cur_ind, hops_left)]
        
        counts = 0
        for nbr in self.nbrs(cur_ind):
            res = self.hopper(nbr, hops_left-1, memo)
            counts += res
            memo[(nbr, hops_left-1)] = res
            
        return counts
    
    
    def nbrs(self, ind):
        nbrs = {0: [4,6],
                1: [6, 8],
                2: [9, 7],
                3: [4, 8],
                4: [3, 9, 0],
                5: [],
                6: [1,7, 0],
                7: [6, 2],
                8: [1, 3],
                9: [4, 2]}
        
        return nbrs[ind]


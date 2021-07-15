class Solution:
    def knightDialer(self, N: int) -> int:
#         if N < 1: return 0
#         modnum = 10**9 + 7
#         memo = defaultdict(lambda:0)

#         def dfs(y, x, cnt):
#             nonlocal modnum, memo, N
#             if (y,x) == (3,0) or (y,x) == (3,2):
#                 return 0
#             elif cnt == N:
#                 return 1
#             elif (y, x, cnt) in memo:
#                 return memo[(y, x, cnt)]
            
#             tmpcnt = 0

#             for (nxy, nxx) in ((y-1, x-2), (y-2, x-1), (y-2, x+1), (y-1, x+2), (y+1, x+2), (y+2, x+1), (y+2, x-1), (y+1, x-2)):
#                 if(0<=nxy<4 and 0<=nxx<3):
#                     tmpcnt += dfs(nxy, nxx, cnt+1)
#                     tmpcnt %= modnum
            
#             memo[(y, x, cnt)] = tmpcnt
#             return memo[(y, x, cnt)]
            
#         return sum(dfs(y,x,1) for y in range(4) for x in range(3))%modnum
        
        #超级快的版本
    #     self.moves = [(4,6),(6,8),(7,9),(4,8),(3,9,0),(),(1,7,0),(2,6),(1,3),(2,4)]
    #     return sum(self.dfs(N, i) for i in range(10)) % (10**9+7)
    # def dfs(self, N, i, dp={}):
    #     if N == 1: return 1
    #     if (N,i) not in dp:
    #         dp[(N,i)] = sum(self.dfs(N-1, j) for j in self.moves[i])%(10**9+7)
    #     return dp[(N,i)]
        
        #O(N) solution no dfs
        if N == 1: return 10;
        # current number of hops that end in index i, skip 5 because it is terminal
        ends_in = [0 if i == 5 else 1 for i in range(10)]
        mod = 1e9+7
        
        for i in range(N-1):
            next_ends_in = [0 for _ in range(10)]
            next_ends_in[0] = (ends_in[4] + ends_in[6]) % mod
            next_ends_in[1] = (ends_in[6] + ends_in[8]) % mod
            next_ends_in[2] = (ends_in[7] + ends_in[9]) % mod
            next_ends_in[3] = (ends_in[4] + ends_in[8]) % mod
            next_ends_in[4] = (ends_in[3] + ends_in[9] + ends_in[0]) % mod
            # skip 5 because we can never get to it
            next_ends_in[6] = (ends_in[1] + ends_in[7] + ends_in[0]) % mod
            next_ends_in[7] = (ends_in[2] + ends_in[6]) % mod
            next_ends_in[8] = (ends_in[1] + ends_in[3]) % mod
            next_ends_in[9] = (ends_in[2] + ends_in[4]) % mod
            ends_in = next_ends_in
        
        return int(sum(ends_in) % mod)
        
        
        
        
        
        
        
        


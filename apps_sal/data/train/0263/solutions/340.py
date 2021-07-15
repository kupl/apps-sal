class Solution:
    def knightDialer(self, N: int) -> int:
        
        jump_map = {1:[6,8],
                   2:[7,9],
                   3:[4,8],
                   4:[3,9,0],
                   5: [],
                   6: [1,7,0],
                   7:[6,2],
                   8:[1,3],
                   9:[2,4],
                   0:[4,6]}
        
        dp_map = {}
        
        def get_num(s, n):
            if (s,n) not in dp_map:
                if n == 1:
                    dp_map[(s,n)] = 1
                    return dp_map[(s,n)]
                ans = 0
                for target in jump_map[s]:
                    ans += get_num(target, n-1)
                dp_map[(s,n)] = ans
            return dp_map[(s,n)]
            
        total = 0
        for i in jump_map.keys():
            total += get_num(i, N)
            
        return total % (10**9 + 7)

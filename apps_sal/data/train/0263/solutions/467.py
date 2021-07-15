class Solution:
    def knightDialer(self, left: int) -> int:
        moves = [(2,-1),(2,1),(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2)]
        n = 4
        m = 3
        @lru_cache(None)
        def back(i,j,left):
            if left==1:
                return 1
            ans = 0
            for a,b in moves:
                if 0<=i+a<n and 0<=j+b<m and (i+a,j+b)!=(3,0) and (i+a,j+b)!=(3,2):
                    ans+=back(i+a, j+b, left-1)
            return ans
        main = 0
        for i in range(3):
            for j in range(3):
                main+= back(i,j, left)
        main+=back(3, 1,left)
        
        return main%(10**9+7)

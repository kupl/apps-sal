class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[-sys.maxsize for i in range(n)] for j in range(n)]
        
        def DFS(left:int,right:int)->int:
            if memo[left][right]!=-sys.maxsize:
                return memo[left][right]
            if left>=right:
                return 0
            score = max(piles[left]-DFS(left+1,right),piles[right]-DFS(left,right-1))
            memo[left][right] = score
            return score
        
        
        return True if DFS(0,n-1)>0 else False

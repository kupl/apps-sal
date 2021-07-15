class Solution:
    def knightDialer(self, N: int) -> int:
        nos = [[1,2,3], [4,5,6], [7,8,9], [None, 0, None]]
        if N == 0:
            return 0
        
        memo = {}
        
        def calculate(currentIndex, remainingSteps):
            if remainingSteps == 0:
                return 1
            if (currentIndex, remainingSteps) in memo:
                return memo[(currentIndex, remainingSteps)] 
            i, j = currentIndex
            
            possibleMoves = []
            
            if i+2 < 4 and j - 1 >= 0 and nos[i+2][j-1] is not None:
                possibleMoves.append((i+2, j-1))
                
            if i+2 < 4 and j + 1 < 3 and nos[i+2][j+1] is not None:
                possibleMoves.append((i+2, j+1))
            
            if i - 1 >= 0 and j+2 < 3 and nos[i-1][j+2] is not None:
                possibleMoves.append((i-1,j+2))
            
            if i+1 < 4 and j+2 < 3 and nos[i+1][j+2] is not None:
                possibleMoves.append((i+1, j+2))
            
            if i-2 >= 0 and j+1 < 3 and nos[i-2][j+1] is not None:
                possibleMoves.append((i-2,j+1))
            
            if i-2 >=0 and j-1 >= 0 and nos[i-2][j-1] is not None:
                possibleMoves.append((i-2, j-1))
            
            if i-1>=0 and j-2>=0 and nos[i-1][j-2] is not None:
                possibleMoves.append((i-1,j-2))
                
            if i+1 < 4 and j-2 >=0 and nos[i+1][j-2] is not None:
                possibleMoves.append((i+1,j-2))
                
            if remainingSteps == 1:
                memo[(currentIndex, remainingSteps)]  = len(possibleMoves)
                return len(possibleMoves) 
            
            
            
            totalNos = 0
            
            for nextInd in possibleMoves:
                totalNos += calculate(nextInd, remainingSteps-1)
                # if totalNos >= 10**9 + 7:
                #     totalNos = totalNos % (10**9 + 7)
            
            memo[(currentIndex, remainingSteps)] = totalNos
            return memo[(currentIndex, remainingSteps)] 
        
        
        total = 0
        for i in range(0, 4):
            for j in range(0, 3):
                if nos[i][j] is not None:
                    total += calculate((i,j), N-1)
        return total % (10**9 + 7)

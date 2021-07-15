class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        table = [False] * (n+1)
        table[1] = True
        for i in range(2, n+1):
            num = 1
            while num ** 2 <= i:
                square = num ** 2
                if not table[ i - square ]:
                    table[i] = True
                    break
                num += 1
                
        return table[-1]

from collections import Counter

class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {1 : [6, 8],
                 2 : [7, 9],
                 3 : [4, 8],
                 4 : [3, 9, 0],
                 6 : [1, 7, 0],
                 7 : [2, 6],
                 8 : [1, 3],
                 9 : [2, 4],
                 0 : [4, 6],
                }
        if n == 1:
            return 10
        
        starts = Counter([i for i in moves])
        for _ in range(n - 1):
            next = Counter()
            for i in starts:
                for j in moves[i]:
                    next[j] += starts[i]
            starts = next
            
        return sum(starts.values()) % (10 ** 9 + 7)

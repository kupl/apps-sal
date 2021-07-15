possibilities = {
    1: [6,8],
    2: [7,9],
    3: [8,4],
    4: [9,3,0],
    5: [],
    6: [1,7,0],
    7: [6,2],
    8: [1,3],
    9: [2,4],
    0: [4,6],
}


class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10
        
        counter = 0
        num_ways = [1,1,1,1,1,0,1,1,1,1]
        for i in range(N-1):
            updated = [0]*10
            for digit in range(10):
                updated[digit] = sum([num_ways[previous] % int(10e8+7) for previous in possibilities[digit]]) 
            num_ways = updated
        return sum(num_ways) % int(10e8+7)
        
        
        
        
        
        




class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        streak = 0

        for num in arr[1:]:
            if winner > num:
                streak += 1
            
            else:
                winner = num
                streak = 1
            
            if streak == k:
                return winner
        
        return winner


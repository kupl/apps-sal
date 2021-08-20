class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        wins = 0
        for i in range(1, len(arr), 1):
            if winner > arr[i]:
                wins += 1
            else:
                wins = 1
                winner = arr[i]
            if wins == k:
                break
        return winner

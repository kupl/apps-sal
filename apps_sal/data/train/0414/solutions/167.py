class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = {}

        challenger = 1
        while True:
            winner = max(arr[0], arr[challenger])
            loser = max(arr[challenger], arr[0])

            if winner in win_count:
                win_count[winner] += 1
            else:
                win_count[winner] = 1

            if win_count[winner] == k or win_count[winner] > len(arr):
                return winner

            arr[0] = winner
            arr[challenger] = loser

            challenger += 1
            if challenger == len(arr):
                challenger = 1

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        win_count = 0
        while win_count != k:
            a1 = arr[0]
            a2 = arr[1]
            if a1 > a2:
                win_count += 1
                winner = a1
                loser = arr.pop(1)
                arr.append(loser)
            else:
                win_count = 1
                winner = a2
                loser = arr.pop(0)
                arr.append(loser)
        return winner

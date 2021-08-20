class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        ct = 0
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                ct = 1
            else:
                ct += 1
            if ct == k:
                return winner
        return winner

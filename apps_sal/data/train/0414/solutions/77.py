class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) or len(arr) <= 2:
            return max(arr)
        winner = 0
        winner_in_row = 0
        while True:
            if winner_in_row == k:
                break
            if arr[0] > arr[1]:
                winner_in_row += 1
                arr.append(arr.pop(1))
            else:
                winner_in_row = 1
                arr.append(arr.pop(0))
        return arr[0]

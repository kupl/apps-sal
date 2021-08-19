class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        if k >= len(arr):
            return max(arr)
        while True:
            move_pos = 0
            if arr[0] > arr[1]:
                move_pos = 1
                wins += 1
            else:
                wins = 1
            arr.append(arr.pop(move_pos))
            if wins == k:
                return arr[0]

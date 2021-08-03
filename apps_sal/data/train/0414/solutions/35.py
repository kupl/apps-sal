class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        streak = 0
        winner = None
        if k >= len(arr) - 1:
            return max(arr)
        while streak < k:
            if arr[0] > arr[1]:
                winner = arr[0]
                arr.append(arr[1])
                del arr[1]
                streak += 1
            else:
                winner = arr[1]
                arr.append(arr[0])
                del arr[0]
                streak = 1
        return winner

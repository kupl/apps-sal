class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        count = 0
        last_win = None
        while True:
            if arr[0] > arr[1]:
                val = arr[1]
                arr.remove(arr[1])
                arr.append(val)
            else:
                val = arr[0]
                arr.remove(arr[0])
                arr.append(val)
            win = arr[0]
            if win != last_win:
                last_win = win
                count = 1
            else:
                count += 1
            if count == k:
                return win

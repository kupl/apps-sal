class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        win_count = 0
        while win_count < min(len(arr), k):
            if arr[0] > arr[1]:
                val = arr.pop(1)
            else:
                val = arr.pop(0)
                win_count = 0
            win_count += 1
            arr.append(val)
        return arr[0]

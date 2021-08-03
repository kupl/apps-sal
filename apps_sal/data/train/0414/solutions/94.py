class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        win_count = 0
        while win_count < k:
            if arr[0] > arr[1]:
                win_count += 1
            else:
                arr[0], arr[1] = arr[1], arr[0]
                win_count = 1
            temp = arr[1]
            del arr[1]
            arr.append(temp)
        return arr[0]

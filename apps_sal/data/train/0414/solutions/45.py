class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) - 1:
            return max(arr)
        nwin = 0
        while nwin < k and len(arr) > 1:
            if arr[0] > arr[1]:
                nwin += 1
            else:
                arr[0] = arr[1]
                nwin = 1
            arr.pop(1)
        return arr[0]

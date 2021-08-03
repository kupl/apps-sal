class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[1], arr[0])
        cur = 1
        arr[1] = max(arr[1], arr[0])
        i = 2
        while i < len(arr):
            if arr[i] > arr[i - 1]:
                cur = 1
            else:
                cur += 1
                arr[i] = arr[i - 1]
            if cur == k:
                return arr[i]
            i += 1
        return max(arr)

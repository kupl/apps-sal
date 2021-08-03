class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        r = 0
        while 1:
            if arr[0] > arr[1]:
                r = r + 1
                z = arr[1]
                del arr[1]
                arr.append(z)
            else:
                r = 1
                arr.append(arr.pop(0))
            if k == r:
                return arr[0]

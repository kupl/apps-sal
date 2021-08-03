class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wincount = 0
        if k > len(arr) + arr.index(max(arr)):
            return max(arr)
        while wincount < k:
            if arr[0] > arr[1]:
                wincount += 1
                arr.append(arr.pop(1))
            else:
                wincount = 1
                arr.append(arr.pop(0))

        return arr[0]

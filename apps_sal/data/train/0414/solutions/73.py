class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        endCount = k if k < len(arr) else len(arr)
        winCount = 0

        for i in range(len(arr)):
            if arr[0] > arr[1]:
                winCount += 1
                arr.append(arr.pop(1))
            else:
                winCount = 1
                arr.append(arr.pop(0))
            if endCount <= winCount:
                break

        return arr[0]

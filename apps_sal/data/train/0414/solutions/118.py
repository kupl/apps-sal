class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        largestFound = -1
        for i in range(len(arr)):
            if arr[i] > largestFound:
                largestFound = arr[i]
                can = True
                if i == 0:
                    for j in range(i + 1, min(i + k + 1, len(arr))):
                        if arr[j] > arr[i]:
                            can = False
                            break
                else:
                    for j in range(i + 1, min(i + k, len(arr))):
                        if arr[j] > arr[i]:
                            can = False
                            break
                if can:
                    return arr[i]

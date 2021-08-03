class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxval = max(arr)
        win_count = 0
        around = 0
        while (win_count < k):
            if (arr[0] == maxval):
                break
            elif (arr[0] > arr[1]):
                win_count += 1
                arr.append(arr[1])
                del arr[1]
            else:
                win_count = 1
                arr.append(arr[0])
                del arr[0]
            around += 1
        return arr[0]

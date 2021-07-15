class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        timeswon = 0
        while timeswon < k:
            if arr[0] == max_num:
                break
            if arr[0] > arr[1]:
                arr.append(arr[1])
                del arr[1]
                timeswon += 1
            else:
                arr.append(arr[0])
                del arr[0]
                timeswon = 1
        return arr[0]

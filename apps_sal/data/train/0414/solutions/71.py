class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        length = len(arr)
        count = 0
        for i in range(length):
            if arr[0] > arr[1]:
                arr.append(arr[1])
                arr.pop(1)
                count += 1
            else:
                arr.append(arr[0])
                arr.pop(0)
                count = 1
            if count == k:
                break
        return arr[0]

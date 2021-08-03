class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        d = dict()
        count = 0
        while(count < k and count < n):
            if(arr[0] > arr[1]):
                count += 1
                arr.append(arr.pop(1))
            else:
                count = 1
                arr[0], arr[1] = arr[1], arr[0]
                arr.append(arr.pop(1))
        return arr[0]

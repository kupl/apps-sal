class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        c = k
        if len(arr) == 1:
            return arr[0]
        m = max(arr)
        if k == 1:
            return max(arr[1], arr[0])
        while 1:
            if arr[0] == m:
                return arr[0]
            if arr[0] > arr[1]:
                c -= 1
                if c == 0:
                    return arr[0]
                arr.append(arr[1])
                del arr[1]
            else:
                c = k - 1
                arr.append(arr[0])
                del arr[0]

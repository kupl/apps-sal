class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        curr = arr[0]

        count = 0
        if arr[0] > arr[1]:
            v = arr.pop(1)
            arr.append(v)
        else:
            v = arr.pop(0)
            curr = arr[0]
            arr.append(v)
        count += 1

        while count < k:
            new = arr[1]

            if curr > new:
                v = arr.pop(1)
                arr.append(v)
                count += 1
            else:
                v = arr.pop(0)
                arr.append(v)
                count = 1
                curr = arr[0]

        return curr

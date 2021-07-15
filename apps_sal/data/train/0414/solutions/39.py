class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) // 2:
            return max(arr)
        curr = 1
        if arr[0] < arr[1]:
            arr.append(arr.pop(0))
        else:
            arr.append(arr.pop(1))
        while curr < k:
            if arr[0] < arr[1]:
                curr = 1
                arr.append(arr.pop(0))
            else:
                curr += 1
                arr.append(arr.pop(1))
        return arr[0]

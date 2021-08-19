class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        k = min(k, len(arr))
        curr = 0
        count = 0
        for indx in range(len(arr)):
            if arr[curr] == arr[indx]:
                continue
            if arr[indx] < arr[curr]:
                count += 1
            if arr[indx] > arr[curr]:
                count = 1
                curr = indx
            if count >= k:
                return arr[curr]
        return max(arr)

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) < k:
            return max(arr)
        curr = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if curr < arr[i]:
                curr = arr[i]
                count = 1
            else:
                count+=1
            if count == k:
                return curr
        return curr

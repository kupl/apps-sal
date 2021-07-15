class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        mx = max(arr)
        if k>=len(arr):
            return mx
        
        cnt = 0
        for i in range(1, len(arr)):
            if arr[0]<=arr[i]:
                arr[i], arr[0] = arr[0], arr[i]
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                return arr[0]
        
        return mx

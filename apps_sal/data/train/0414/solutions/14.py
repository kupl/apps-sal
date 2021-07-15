class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        cur=arr[0]
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] > cur:
                cur = arr[i]
                cnt = 0
            cnt += 1
            if (cnt == k): break
        return cur


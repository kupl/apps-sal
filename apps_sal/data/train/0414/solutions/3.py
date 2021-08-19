class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

     #   s=[]

        prev = arr[0]
        i = 1
        ans = 0
        while i < len(arr):
            if arr[i] >= prev:
                ans = 0
                prev = arr[i]

            ans += 1
            i += 1
            # print(ans)
            if ans == k:
                return prev
        return prev

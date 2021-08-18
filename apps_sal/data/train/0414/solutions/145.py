class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        ans = 0
        curr = 0
        for i in range(1, len(arr)):
            if ans == k:
                break
            if curr < max(arr[i - 1], arr[i]):
                ans = 0

            curr = max(curr, max(arr[i - 1], arr[i]))
            ans += 1

        return curr

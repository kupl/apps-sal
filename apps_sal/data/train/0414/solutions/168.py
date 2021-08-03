class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        maxi = max(arr)
        if k >= n - 1:
            return maxi

        l = 0
        r = 1
        count = 0
        while r < n:
            if arr[r] == maxi or arr[l] == maxi:
                return maxi
            if arr[r] < arr[l]:
                r += 1
                count += 1
            else:
                l = r
                count = 1
                r += 1

            if count >= k:
                return arr[l]

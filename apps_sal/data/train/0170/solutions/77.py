class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        while 0 < r and arr[r - 1] <= arr[r]:
            r -= 1

        ret = r
        while l == 0 or l < n and arr[l - 1] <= arr[l]:
            while r <= l or r < n and arr[r] < arr[l]:
                r += 1
            ret = min(ret, r - l - 1)
            l += 1

        return ret

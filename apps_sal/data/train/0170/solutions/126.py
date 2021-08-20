class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        ret = r
        l = 0
        for l in range(len(arr)):
            if l > 0 and arr[l] < arr[l - 1]:
                break
            if l >= r:
                break
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            print((l, r))
            ret = min(ret, r - l - 1)
        return ret

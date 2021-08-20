import bisect


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        a = 0
        for i in range(len(arr)):
            if i == 0 or arr[i] >= arr[i - 1]:
                a += 1
            else:
                break
        b = 0
        for i in reversed(list(range(len(arr)))):
            if i == len(arr) - 1 or arr[i] <= arr[i + 1]:
                b += 1
            else:
                break
        if a == len(arr):
            return 0
        al = arr[:a]
        bl = arr[len(arr) - b:]
        ans = len(arr) - 1
        for i in range(a):
            target = al[i]
            index = bisect.bisect_left(bl, target)
            if index == len(bl):
                ans = min(ans, len(arr) - i - 1)
            else:
                ans = min(ans, len(arr) - (i + 1) - (len(bl) - index))
        ans = min(ans, len(arr) - len(bl))
        return ans

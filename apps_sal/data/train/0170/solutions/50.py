from bisect import bisect_right


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                u = i
                break
        else:
            return 0

        for j in range(len(arr) - 1, -1, -1):
            if arr[j] < arr[j - 1]:
                v = j
                break

        arr1 = arr[:u + 1]
        arr2 = arr[v:]
        print(arr1, arr2)
        ans = len(arr)
        for i in range(len(arr2)):
            ans = min(ans, len(arr) - (bisect_right(arr1, arr2[i]) + 1 + len(arr2) - i - 1))
        return min(ans, len(arr) - len(arr1), len(arr) - len(arr2))

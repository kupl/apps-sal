class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
        for i1 in range(len(arr) - 1):
            if arr[i1 + 1] >= arr[i1]:
                continue
            else:
                break
        if arr[-2] <= arr[-1] and i1 == len(arr) - 2:
            return 0
        for i2 in range(len(arr) - 1, 0, -1):
            if arr[i2] >= arr[i2 - 1]:
                continue
            else:
                break
        print(i1, i2)
        remove = i2 - 1 - (i1 + 1) + 1
        ans = min(remove + i1 + 1, remove + len(arr) - i2)
        for i in range(i1, -1, -1):
            num = arr[i]
            l, r = i2, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] >= num:
                    r = mid
                else:
                    l = mid + 1
            if l < len(arr):
                cur = remove + i1 - i + l - i2
                ans = min(cur, ans)
        return ans

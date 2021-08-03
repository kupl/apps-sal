class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        before = n
        after = 0
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                before = i - 1
                break
        if before == n:
            return 0
        for i in range(n - 1)[::-1]:
            if arr[i] > arr[i + 1]:
                after = i + 1
                break
        l, r = 0, n
        while l < r:
            m = l + (r - l) // 2
            ok = before >= n - 1 - m or after <= m

            for start in range(1, n):
                if start + m >= n:
                    break
                else:
                    left = before >= start - 1
                    right = after <= start + m
                    ok |= left and right and arr[start - 1] <= arr[start + m]
            if ok:
                r = m
            else:
                l = m + 1
        return l

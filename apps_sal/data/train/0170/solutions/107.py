class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        answer = n
        curr = arr[0]
        start = 1
        while start < n:
            if arr[start] >= curr:
                curr = arr[start]
                start += 1
            else:
                break
        start -= 1
        if start == n - 1:
            return 0
        curr = arr[n - 1]
        end = n - 2
        while end >= 0:
            if arr[end] <= curr:
                curr = arr[end]
                end -= 1
            else:
                break
        end += 1
        answer = min(answer, n - start - 1, end)
        (l, r) = (0, end)
        while r < n and l <= start:
            if arr[l] <= arr[r]:
                answer = min(answer, r - l - 1)
                l += 1
            else:
                r += 1
        return answer

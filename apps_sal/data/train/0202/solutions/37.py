class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        a = A
        start = 0
        end = 0
        maxlen = 0
        n = len(a)
        while(start < n - 1 and end < n):
            end = start
            if a[start] < a[start + 1]:
                while end < n - 1 and a[end] < a[end + 1]:
                    end += 1
                if end < n - 1 and a[end] > a[end + 1]:
                    while(end < n - 1 and a[end] > a[end + 1]):
                        end += 1
                    maxlen = max(maxlen, end - start + 1)
            start = max(start + 1, end)

        return maxlen

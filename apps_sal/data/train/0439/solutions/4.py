class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        (start, end) = (1, 1)
        maxLen = 1
        while start < len(A):
            end = start
            while end < len(A):
                if end % 2 == 0 and A[end] > A[end - 1]:
                    end += 1
                elif end % 2 != 0 and A[end] < A[end - 1]:
                    end += 1
                else:
                    break
            print((start, end))
            maxLen = max(maxLen, end - start + 1)
            if start == end:
                start = end + 1
            else:
                start = end
        (start, end) = (1, 1)
        while start < len(A):
            end = start
            while end < len(A):
                if end % 2 == 0 and A[end] < A[end - 1]:
                    end += 1
                elif end % 2 != 0 and A[end] > A[end - 1]:
                    end += 1
                else:
                    break
            print((start, end))
            maxLen = max(maxLen, end - start + 1)
            if start == end:
                start = end + 1
            else:
                start = end
        return maxLen

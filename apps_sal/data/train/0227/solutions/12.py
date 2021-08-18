class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = 0
        l = len(A)
        count = 0
        max_len = 0
        while end < l:
            if A[end] == 1:
                max_len = max(max_len, end - start + 1)
                end = end + 1
            else:
                if count < K:
                    max_len = max(max_len, end - start + 1)
                    count = count + 1
                    end = end + 1
                else:
                    while start <= end and count >= K:
                        if A[start] == 0:
                            count = count - 1
                        start = start + 1

        return max_len

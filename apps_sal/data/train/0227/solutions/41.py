class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        contains = 0
        max_len = 0

        while right < len(A):
            if A[right] == 0:
                contains += 1

                if contains > K:
                    while contains > K:
                        if A[left] == 0:
                            contains -= 1
                        left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

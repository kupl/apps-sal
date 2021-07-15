class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        length = len(A)
        if length < L + M:
            return 0
        if length == L + M:
            return sum(A)
        res = 0
        for i in range(length - L + 1):
            s1 = sum(A[i:i+L])
            if i >= M:
                for j in range(i-M+1):
                    s2 = sum(A[j:j+M])
                    if res < s1 + s2:
                        res = s1 + s2
                for j in range(i + L, length - M + 1):
                    s2 = sum(A[j:j+M])
                    if res < s1 + s2:
                        res = s1 + s2
            else:
                for j in range(i + L, length - M + 1):
                    s2 = sum(A[j:j+M])
                    if res < s1 + s2:
                        res = s1 + s2
        return res


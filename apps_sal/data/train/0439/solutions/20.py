class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        maxlen = sublen = 0
        for i in range(len(A)):
            if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
                sublen += 1
            elif i >= 1 and A[i-1] != A[i]:
                sublen = 2
            else:
                sublen = 1
            maxlen = max(maxlen, sublen)
        return maxlen


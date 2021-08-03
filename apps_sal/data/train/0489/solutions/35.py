class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        s = []

        for i in range(len(A)):
            if(not s or A[s[-1]] > A[i]):
                s.append(i)

        j = len(A) - 1
        res = 0
        while(j > res):
            while(s and A[j] >= A[s[-1]]):
                i = s.pop()
                res = max(res, j - i)
            j -= 1
        return res

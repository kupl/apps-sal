class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        l = len(A)
        left = [0 for _ in range(l)]
        right = [0 for _ in range(l)]
        s = []
        res = 0
        for i in range(l):
            if s:
                if A[i] < A[s[-1]]:
                    while s and A[i] < A[s[-1]]:
                        s.pop()
                    if s == []:
                        left[i] = i
                    else:
                        left[i] = i - s[-1] - 1
            s.append(i)
        A.reverse()
        s.clear()
        for i in range(l):
            if s:
                if A[i] <= A[s[-1]]:
                    while s and A[i] <= A[s[-1]]:
                        s.pop()
                    if s == []:
                        right[i] = i
                    else:
                        right[i] = i - s[-1] - 1
            s.append(i)
        for i in range(l):
            if left[i] == 0 and right[l - 1 - i] == 0:
                res += A[l - 1 - i]
            else:
                res += A[l - 1 - i] * (left[i] + 1) * (right[l - 1 - i] + 1)
        return res % (10**9 + 7)

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        l = len(A)
        left = [0 for _ in range(l)]
        right = [0 for _ in range(l)]
        s = []
        res = 0
        for i in range(l):
            if s:
                if A[i] > A[s[-1]]:
                    s.append(i)
                else:
                    while s and A[i] < A[s[-1]]:
                        pre = s.pop()
                    if s == []:
                        left[i] = i
                    else:
                        left[i] = i - s[-1] - 1
                    s.append(i)
            else:
                s.append(i)
        A = A[::-1]
        s = []
        for i in range(l):
            if s:
                if A[i] > A[s[-1]]:
                    s.append(i)
                else:
                    while s and A[i] <= A[s[-1]]:
                        pre = s.pop()
                    if s == []:
                        right[i] = i
                    else:
                        right[i] = i - s[-1] - 1
                    s.append(i)
            else:
                s.append(i)
        right = right[::-1]
        A = A[::-1]
        for i in range(l):
            res += A[i] * (left[i] + 1) * (right[i] + 1)
        return res % (10**9 + 7)

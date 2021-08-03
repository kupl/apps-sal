class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        space = len(A) - L - M
        maxx = 0
        for i in range(1, space + 2):
            a = 0
            b = L - 1
            c = b + i
            d = c + M - 1
            leftSum = sum(A[a:b + 1])
            rightSum = sum(A[c:d + 1])
            while d < len(A):
                maxx = max(maxx, leftSum + rightSum)
                a += 1
                b += 1
                c += 1
                d += 1
                if d < len(A):
                    leftSum -= A[a - 1]
                    leftSum += A[b]
                    rightSum -= A[c - 1]
                    rightSum += A[d]
        maxx2 = 0
        for i in range(1, space + 2):
            a = 0
            b = M - 1
            c = b + i
            d = c + L - 1
            leftSum = sum(A[a:b + 1])
            rightSum = sum(A[c:d + 1])
            while d < len(A):
                maxx2 = max(maxx2, leftSum + rightSum)
                a += 1
                b += 1
                c += 1
                d += 1
                if d < len(A):
                    leftSum -= A[a - 1]
                    leftSum += A[b]
                    rightSum -= A[c - 1]
                    rightSum += A[d]

        return max(maxx, maxx2)

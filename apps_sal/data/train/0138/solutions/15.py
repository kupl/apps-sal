class Solution:
    def getMaxLen(self, A: List[int], cnt=0, best=0) -> int:
        A.append(0)
        N = len(A)
        i = 0
        j = 0
        while i < N:
            while j < N and not A[j]:
                while i < j:
                    cnt = cnt - 1 if A[i] < 0 else cnt
                    i += 1
                    best = best if cnt & 1 else max(best, j - i)
                i = j + 1
                j = j + 1
            while j < N and A[j]:
                cnt = cnt + 1 if A[j] < 0 else cnt
                j += 1
                best = best if cnt & 1 else max(best, j - i)
        return best

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        i = 0
        j = 0
        A.sort()
        while i < len(A) and A[i] <= 0:
            if A[i] % 2 != 0:
                return False
            while j < len(A) and A[j] < 0 and 2 * A[j] < A[i]:
                j += 1
            if j >= len(A) or 2 * A[j] > A[i]:
                return False
            A[j] = None
            j += 1
            i += 1
            while i < len(A) and A[i] is None:
                i += 1
                
        while i < len(A):
            while j < len(A) and A[j] < 2 * A[i]:
                j += 1
            if j >= len(A) or A[j] > 2 * A[i]:
                return False
            A[j] = None
            j += 1
            i += 1
            while i < len(A) and A[i] is None:
                i += 1
        return True

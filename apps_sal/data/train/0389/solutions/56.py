from fractions import Fraction
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if len(A) == 1: return False
        avg = Fraction(sum(A), len(A))
        A = [num - avg for num in A]
        left = set()
        for i in range(len(A) // 2):
            curr_set = {s + A[i] for s in left}
            left = left | curr_set | {A[i]}
        if 0 in left: return True
        rsum = sum(A[i] for i in range(len(A) // 2, len(A)))
        right = set()
        for i in range(len(A) // 2, len(A)):
            if A[i] == 0: return True
            curr_set = {A[i]}
            for s in right:
                if s + A[i] == 0 or (- s - A[i] in left and s + A[i] != rsum):
                    return True
                curr_set.add(s + A[i])
            right = right | curr_set
        return False

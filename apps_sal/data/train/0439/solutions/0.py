class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1: return 1
        prev = A[1]
        maxcount = count = 1 + int(A[0] != A[1])
        print(count)
        lastcomp = A[0] < A[1]
        
        for a in A[2:]:
            comp = prev < a
            if prev == a:
                count = 0
            elif comp == lastcomp:
                count = 1
            lastcomp = comp
            count += 1
            maxcount = max(maxcount, count)
            prev = a
        return maxcount

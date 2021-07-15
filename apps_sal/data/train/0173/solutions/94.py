# O(nlogn)  S(n)
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        A = [a % k for a in arr]
        A.sort()
        l = 0
        r = len(A) - 1
        while l < len(A) and A[l] == 0:
            l += 1
        if l % 2 == 1:
            return False
        while l < r:
            if A[l] + A[r] != k:
                return False
            l += 1
            r -= 1
        return True

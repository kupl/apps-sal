class Solution:
    def canArrange(self, A: List[int], k: int) -> bool:
        A.sort(key=lambda x: x % k, reverse=True)
        i, n = 1, len(A)

        while i < len(A) and A[-i] % k == 0:
            if A[-i - 1] % k:
                return False
            else:
                i += 2

        if i < len(A):
            j = 0
            i0 = i
            while A[-i] % k and j < (n - i0 + 1) // 2:
                if (A[-i] + A[j]) % k:
                    return False
                i += 1
                j += 1

        return True

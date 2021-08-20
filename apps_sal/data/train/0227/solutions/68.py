class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (s, e) = (0, 0)
        r_k = K
        result = 0
        while e < len(A):
            if A[e] == 0:
                r_k -= 1
            while r_k < 0:
                if A[s] == 0:
                    r_k += 1
                s += 1
            result = max(result, e - s + 1)
            e += 1
        return result

class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        mul_result = {}

        def get_mul(high, low):
            if high == -1 or low == -1:
                return 0
            if (high, low) in mul_result:
                return mul_result[high, low]
            result = get_mul(high - 1, low - 1)
            if A[high] in B[:low + 1]:
                for i in range(low, -1, -1):
                    if B[i] == A[high]:
                        break
                result = max(result, get_mul(high - 1, i - 1) + 1)
            if B[low] in A[:high + 1]:
                for i in range(high, -1, -1):
                    if A[i] == B[low]:
                        break
                result = max(result, get_mul(i - 1, low - 1) + 1)
            mul_result[high, low] = result
            return result
        return get_mul(len(A) - 1, len(B) - 1)

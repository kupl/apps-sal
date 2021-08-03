class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        z_count = 0
        l = 0
        result = 0
        for i in range(len(A)):
            if not A[i]:
                z_count += 1
            if z_count <= K:
                result = max(result, i - l + 1)
            while l < i and z_count > K:
                if not A[l]:
                    z_count -= 1
                l += 1

        return result

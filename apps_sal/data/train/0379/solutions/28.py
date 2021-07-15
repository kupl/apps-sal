class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        i = j = 0
        s1 = s2 = 0
        MOD = 10 ** 9 + 7
        while i < len(A) or j < len(B):
            if i < len(A) and (j == len(B) or A[i] < B[j]):
                s1 += A[i]
                i += 1
            elif j < len(B) and (i == len(A) or A[i] > B[j]):
                s2 += B[j]
                j += 1
            else:
                s1 = s2 = (max(s1, s2) + A[i]) % MOD
                i += 1
                j += 1
        return max(s1, s2) % MOD
        
    
    def maxSum_foolish_DP(self, A: List[int], B: List[int]) -> int:
        N = [A, B]
        NN = [{v : i for i, v in enumerate(A)}, {v : i for i, v in enumerate(B)}]

        @functools.lru_cache(None)
        def helper(index, is_bottom, changed):
            nonlocal N, NN
            if index < 0:
                return 0

            value = N[is_bottom][index]
            if changed:
                if value not in NN[1 ^ is_bottom]:
                    return float('-inf')
                return helper(NN[1 ^ is_bottom][value], 1 ^ is_bottom, 0)
            else:
                return value + max(helper(index - 1, is_bottom, 0), helper(index - 1, is_bottom, 1))
        
        return (max(helper(len(A) - 1, 0, 0), helper(len(A) - 1, 0, 1), helper(len(B) - 1, 1, 0), helper(len(B) - 1, 1, 1))) % (10 ** 9 + 7)

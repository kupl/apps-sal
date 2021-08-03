class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = {}
        return self.helper(0, 0, A, B, memo)

    def helper(self, a_index, b_index, A, B, memo):
        if a_index == len(A) or B == len(B):
            return 0
        elif (a_index, b_index) in memo:
            return memo[(a_index, b_index)]
        else:
            put_ = 0
            noput_ = 0
            for i in range(b_index, len(B)):
                if B[i] == A[a_index]:
                    put_ = 1 + self.helper(a_index + 1, i + 1, A, B, memo)
                    break
            noput_ = self.helper(a_index + 1, b_index, A, B, memo)
            memo[(a_index, b_index)] = max(put_, noput_)
            return memo[(a_index, b_index)]

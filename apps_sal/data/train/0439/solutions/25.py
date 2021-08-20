class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        return self.sb(A)

    def sb(self, A):
        if len(A) < 2:
            return len(A)
        (ans, temp_ans) = (1, 1)
        prev_pos = '?'
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and prev_pos in '<?' or (A[i] < A[i - 1] and prev_pos in '>?'):
                temp_ans += 1
                prev_pos = '>' if A[i] > A[i - 1] else '<'
            else:
                temp_ans = 2 if A[i] != A[i - 1] else 1
                prev_pos = '>' if A[i] > A[i - 1] else '<'
            ans = max(ans, temp_ans)
        return ans

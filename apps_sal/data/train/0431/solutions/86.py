class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:

        stack = []
        mult = 0
        ans = 0

        for curr_val in A:
            curr_cnt = 1
            while stack and stack[-1][0] >= curr_val:
                val_p, cnt_p = stack.pop()
                curr_cnt += cnt_p
                mult -= val_p * cnt_p
            stack.append((curr_val, curr_cnt))
            mult += curr_val * curr_cnt
            ans += mult
        return ans % (10**9 + 7)

        # Two-Pass
#         CNT = 0
#         VAL = 1
#         N = len(A)
#         left = [0] * N
#         right = [0] * N

#         def sum_of_single_min(idx):
#             return A[idx] * left[idx] * right[idx]

#         stack = []
#         for i, curr_val in enumerate(A):
#             curr_cnt = 1
#             while stack and stack[-1][VAL] > curr_val:
#                 curr_cnt += stack.pop()[CNT]
#             stack.append((curr_cnt, curr_val))
#             left[i] = curr_cnt

#         stack = []
#         for i in range(N-1, -1, -1):
#             curr_val = A[i]
#             curr_cnt = 1
#             while stack and stack[-1][VAL] >= curr_val:
#                 curr_cnt += stack.pop()[CNT]
#             stack.append((curr_cnt, curr_val))
#             right[i] = curr_cnt

#         return sum(sum_of_single_min(i) for i in range(N)) % (10**9 + 7)

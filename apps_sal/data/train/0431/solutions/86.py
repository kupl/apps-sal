class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        mult = 0
        ans = 0
        for curr_val in A:
            curr_cnt = 1
            while stack and stack[-1][0] >= curr_val:
                (val_p, cnt_p) = stack.pop()
                curr_cnt += cnt_p
                mult -= val_p * cnt_p
            stack.append((curr_val, curr_cnt))
            mult += curr_val * curr_cnt
            ans += mult
        return ans % (10 ** 9 + 7)
